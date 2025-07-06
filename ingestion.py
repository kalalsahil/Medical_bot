from dataIngestion.extraction import extract_data
from dataIngestion.embedding import embed_data
import os

if __name__=="__main__":
    data_dir = "./raw_docs"

    # Loop through all PDF files in the directory
    for filename in os.listdir(data_dir):
        if filename.endswith(".pdf"):
            fpath = os.path.join(data_dir, filename)

            llama_docs = extract_data(fpath)
            embed_data(llama_docs)

    print("All PDF files have been ingested.")