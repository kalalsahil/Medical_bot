from utils.logger import logging
from llama_index.core import VectorStoreIndex
from dataIngestion.utils import storage_context


def embed_data(llama_docs):
    index = VectorStoreIndex.from_documents(
        llama_docs, storage_context=storage_context, show_progress=True
    )
    
    logging.info("Data embedded successfully...")
    