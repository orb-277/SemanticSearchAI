# SemanticSearchAI
# Embedding-based Search with Cohere's Embedding API and Pinecone

This repository provides an example implementation of embedding-based search using Cohere's Embedding API and Pinecone as the vector database. The system allows you to find the most semantically similar embeddings using cosine similarity metric. The web deployment is done using Flask and Jinja.

## Overview

Embedding-based search is a powerful technique that enables efficient retrieval of semantically similar items. This repository demonstrates how to leverage Cohere's Embedding API and Pinecone to perform such searches. The system consists of two main components:

1. **Cohere's Embedding API**: Cohere's Embedding API is used to obtain embeddings for a given text or document. It uses state-of-the-art natural language processing models to encode textual inputs into high-dimensional vector representations.

2. **Pinecone**: Pinecone is a vector database that allows fast similarity searches on high-dimensional embeddings. It provides an efficient and scalable solution for storing and querying embeddings.

## Features

- Obtain embeddings for text using Cohere's Embedding API.
- Store and index embeddings in Pinecone's vector database.
- Perform similarity searches to find the most semantically similar embeddings.
- Web deployment using Flask and Jinja, allowing users to interact with the system through a user-friendly interface.

## Getting Started

To get started with this repository, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Cohere's API key:

   - Obtain an API key from Cohere's website.
   - Set the `COHERE_API_KEY` environment variable to your API key.

4. Set up Pinecone:

   - Sign up for a Pinecone account and create an index.
   - Set the `PINECONE_API_KEY` and `PINECONE_INDEX_NAME` environment variables.

5. Start the Flask application:

   ```bash
   flask --app App run 
   ```

6. Open your web browser and go to `http://localhost:5000` to access the application.

## Usage

1. Upload a text file.
2. Ask it questions to get relevant information.
3. The results will be displayed, showing the closest embeddings based on cosine similarity.

## Customization

Feel free to customize and extend this implementation according to your needs. Some possible improvements and extensions include:

- Adding more advanced search functionalities.
- Integrating with other APIs or databases for additional data sources.
- Improving the user interface and visualizations.

## Contributing

Contributions to this repository are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).
