import os
import logging
from dotenv import load_dotenv
from pymilvus import connections, utility

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


milvus_alias = os.environ.get("MILVUS_ALIAS")
milvus_host = os.environ.get("MILVUS_HOST")
milvus_port = os.environ.get("MILVUS_PORT")
milvus_collection_name = os.getenv("MILVUS_VECTOR_COLLECTION_NAME")

# Validate environment variables
if not all([milvus_alias, milvus_host, milvus_port, milvus_collection_name]):
    logger.error("Missing required environment variables.")
    exit(1)


def drop_collection():
    connections.connect(milvus_alias, host=milvus_host, port=milvus_port)

    if utility.has_collection(milvus_collection_name):
        utility.drop_collection(milvus_collection_name)
        logger.info(f"Collection {milvus_collection_name} dropped.")
    else:
        logger.info(f"Collection {milvus_collection_name} does not exist.")

    connections.disconnect(milvus_alias)


if __name__ == "__main__":
    drop_collection()
