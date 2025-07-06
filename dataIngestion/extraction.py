import pymupdf4llm
from utils.logger import logging
from llama_index.readers.file import PyMuPDFReader

def extract_data(pdf_path):
    
    llama_reader = pymupdf4llm.LlamaMarkdownReader()
    llama_docs = llama_reader.load_data(pdf_path)
    
    logging.info("Data extracted successfully from pdf....")

    print(f"Document Name: {llama_docs[0].metadata}")
    return llama_docs