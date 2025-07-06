import os
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.postprocessor import MetadataReplacementPostProcessor, SentenceTransformerRerank
from llama_index.llms.ollama import Ollama


Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db2 = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db2.get_or_create_collection("medical_db")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

llm = Ollama(
    model="mistral:7b",
    request_timeout=1500.0,
    # Manually set the context window to limit memory usage
    temperature=0.2,
    context_window=2000,
)

Settings.llm = llm

postproc = MetadataReplacementPostProcessor(target_metadata_key="window")
rerank = SentenceTransformerRerank(
        top_n=4, model="BAAI/bge-reranker-base"
    )
query_engine = index.as_query_engine(similarity_top_k=12, node_postprocessors=[postproc, rerank])