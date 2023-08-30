
# Milvus-OpenAI Embeddings Generator

This script generates embeddings for files stored in the `milvus-open-ai/ingestion/data` folder using OpenAI and stores the embeddings in a Milvus collection.

## Prerequisites

- Python 3.9 or higher
- Docker 
- OpenAI API Key
- Local Milvus Docker Container

## Clone the repository

```bash
   git clone https://github.com/sprider/milvus-open-ai.git
```

## Setup virtual environment

Navigate to your project directory and create a virtual environment:

```bash
cd milvus-open-ai/ingestion
python3 -m venv venv
```

This creates a new virtual environment named `venv` in your project directory.

## Activate the virtual environment

Before you can start installing or using packages in your virtual environment you’ll need to activate it. Activating a virtual environment will put the virtual environment-specific `python` and `pip` executables into your shell’s `PATH`.

On macOS and Linux:

```bash
source venv/bin/activate
```

## Install requirements

To install the Python packages that the application depends on, run the following command:

```bash
pip3 install -r requirements.txt
```

## Set environment variables

The application uses several environment variables that you'll need to set. You can set them in your shell, or you can put them in a `.env` file in the ingestion directory of the project. Here's what your `.env` file should look like:

```sh
OPENAI_API_KEY=your-openai-api-key
MILVUS_ALIAS=default
MILVUS_HOST=localhost
MILVUS_PORT=19530
MILVUS_VECTOR_COLLECTION_NAME=your-milvus-collection-name
```

Replace `your-openai-api-key`, and `your-milvus-collection-name` with your actual OpenAI API key, and Milvus collection name.

## Running the script locally

You're now ready to run the scripts.

To ingest the data and generate embeddings for files stored in the `milvus-open-ai/ingestion/data` folder using OpenAI, and then store the embeddings in a Milvus collection, use the following command:

```bash
python3 ingest.py
```

This script will load the documents from the specified directory, split the documents into smaller chunks, generate embeddings for each chunk using OpenAI, and store the embeddings in the Milvus collection specified in the environment variables.

## Running the Script in a Docker Container

Build the Docker image:

```bash
docker build -t milvus_openai_embeddings_generator .
```

Run the Docker container with the necessary environment variables:

```bash
docker run -e OPENAI_API_KEY=your-openai-api-key -e MILVUS_ALIAS=default -e MILVUS_HOST=localhost -e MILVUS_PORT=1950 -e MILVUS_VECTOR_COLLECTION_NAME=your-milvus-collection-name -v $(pwd)/data:/app/data milvus_openai_embeddings_generator
```
