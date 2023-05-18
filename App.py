from flask import Flask,render_template,request,redirect
from config import cohere_api_key,pinecone_api_key
import cohere
import numpy as np
import re
co = cohere.Client(cohere_api_key)
import pinecone
pinecone.init(api_key=pinecone_api_key,environment='asia-southeast1-gcp-free')




app = Flask(__name__)

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/uploader",methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        texts = f.read().decode("utf-8")
        texts = re.split(r'[?!.]', texts)
        texts = [text.strip() for text in texts if text.strip()]
        # f.save(f.filename)
        embeds = co.embed(texts=texts,model='small',truncate='LEFT').embeddings
        # if the index does not exist, we create it
        index_name = 'cohere-pinecone-trec'
        if index_name not in pinecone.list_indexes():
            
            
            pinecone.create_index(
                index_name,
                dimension=1024,
                metric='cosine'
            )



        index = pinecone.Index(index_name)

        ids = [str(i) for i in range(len(texts))]
        
        meta = [{'text': text} for text in texts]

        # create list of (id, vector, metadata) tuples to be upserted
        print(len(embeds))
        
        to_upsert = list(zip(ids, embeds, meta))

        for i in range(0,len(texts)):
            index.upsert(vectors=to_upsert)
        return redirect('/query')

@app.route("/query",methods=['GET','POST'])
def query():
    return render_template('query.html')

@app.route("/queryrun",methods=['GET','POST'])
def queryrun():
    index_name = 'cohere-pinecone-trec'
    index = pinecone.Index(index_name)
    
    index_stats_response = index.describe_index_stats()
    print(index_stats_response)
    if request.method == 'POST':
        query = request.form.get('query')
        k = request.form.get('best_matches')
    xq = co.embed(
    texts=[query],
    model='small',
    truncate='LEFT'
    ).embeddings
    res = index.query(xq, top_k=int(k), include_metadata=True)
    print(res)
    list = []
    for match in res['matches']:
        list.append(match['metadata']['text'])
        #print(f"{match['score']:.2f}: {match['metadata']['text']}")
    return list


