import os
import logging
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

open_api_key = os.environ.get("OPENAI_API_KEY")
milvus_alias = os.environ.get("MILVUS_ALIAS")
milvus_host = os.environ.get("MILVUS_HOST")
milvus_port = os.environ.get("MILVUS_PORT")
milvus_collection_name = os.getenv("MILVUS_VECTOR_COLLECTION_NAME")

# Validate environment variables
if not all(
    [open_api_key, milvus_alias, milvus_host, milvus_port, milvus_collection_name]
):
    logger.error("Missing required environment variables.")
    exit(1)


def load_docs(directory_path):
    try:
        loader = DirectoryLoader(directory_path)
        documents = loader.load()
        return documents
    except Exception as e:
        logger.error(f"Failed to load documents: {e}")
        return []


def split_docs(documents, chunk_size=500, chunk_overlap=20):
    try:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        docs = text_splitter.split_documents(documents)
        return docs
    except Exception as e:
        logger.error(f"Failed to split documents: {e}")
        return []


def store_embeddings_in_milvus(docs):
    try:
        openai_embedding_model = OpenAIEmbeddings(openai_api_key=open_api_key)
        milvus_db = Milvus.from_documents(
            documents=[],
            embedding=openai_embedding_model,
            connection_args={"host": milvus_host, "port": milvus_port},
            collection_name=milvus_collection_name,
            search_params={"metric": "IP", "offset": 0},
        )
        milvus_db.add_documents(documents=docs)
    except Exception as e:
        logger.error(f"Failed to store embeddings in Pinecone: {e}")


def main():
    documents = load_docs("data/")
    if not documents:
        logger.error("No documents loaded.")
        exit(1)
    docs = split_docs(documents)
    if not docs:
        logger.error("No documents split.")
        exit(1)
    store_embeddings_in_milvus(docs)


if __name__ == "__main__":
    main()
