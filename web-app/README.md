# Milvus-OpenAI Conversational Retrieval

This Flask app uses OpenAI and Milvus Open Source Database to provide conversational retrieval functionality. It retrieves relevant responses based on user input.

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
cd milvus-open-ai/web-app
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

The application uses several environment variables that you'll need to set. You can set them in your shell, or you can put them in a `.env` file in the web-app directory of the project. Here's what your `.env` file should look like:

```sh
OPENAI_API_KEY=your-openai-api-key
MILVUS_ALIAS=default
MILVUS_HOST=localhost
MILVUS_PORT=19530
MILVUS_VECTOR_COLLECTION_NAME=your-milvus-collection-name
```

Replace `your-openai-api-key`, and `your-milvus-collection-name` with your actual OpenAI API key, and Milvus collection name.

## Running the app locally

Run the Flask app:

```bash
python3 app.py
```

The app will start on `http://localhost:5000`.

## Running the app in a Docker container

Build the Docker image:

```bash
docker build -t milvus_openai_conversational_retrieval .
```

Run the Docker container with the necessary environment variables:

```bash
docker run -e OPENAI_API_KEY=your-openai-api-key -e MILVUS_ALIAS=default -e MILVUS_HOST=localhost -e MILVUS_PORT=1950 -e MILVUS_VECTOR_COLLECTION_NAME=your-milvus-collection-name -p 5000:5000 milvus_openai_conversational_retrieval
```

The app will be accessible at `http://localhost:5000`.
