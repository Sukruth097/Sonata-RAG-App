# import chromadb
# from langchain.vectorstores import Chroma
from langchain_chroma import Chroma
# from langchain.embeddings.openai import OpenAIEmbeddings
from config import Config
from langchain_openai import AzureOpenAIEmbeddings
import os
# import chromadb.utils.embedding_functions as embedding_functions
os.environ["AZURE_OPENAI_API_KEY"]=Config.AZURE_OPENAI_API_KEY
# os.environ['LANGSMITH_PROJECT']="Sonata-RAG-Management-System"
# os.environ["LANGSMITH_API_KEY"] = Config.LANGSMITH_API_KEY
# os.environ["LANGSMITH_TRACING"] = "true"
# os.environ['LANGSMITH_ENDPOINT'] ="https://api.smith.langchain.com"

class VectorStore:
    def __init__(self,path):
        # self.embeddings= openai_ef = embedding_functions.OpenAIEmbeddingFunction(
        #         api_key="YOUR_API_KEY",
        #         api_base="YOUR_API_BASE_PATH",
        #         api_type="azure",
        #         api_version="YOUR_API_VERSION",
        #         model_name="text-embedding-3-small"
        #     )
        self.embeddings = AzureOpenAIEmbeddings(
            azure_deployment="text-embedding-ada-002",
            azure_endpoint=Config.AZURE_OPENAI_API_ENDPOINT,
            # api_key=Config.AZURE_OPENAI_API_KEY,
            openai_api_version="2023-05-15"
        )
        self.vector_store = Chroma(
            collection_name='rag',
            persist_directory=path,
            embedding_function=self.embeddings
        )

    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
        
    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)

                   