from langchain_openai import AzureChatOpenAI
# from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from config import Config
import os

# os.environ["LANGSMITH_API_KEY"] = Config.LANGSMITH_API_KEY
# os.environ["LANGSMITH_TRACING"] = "true"
os.environ["AZURE_OPENAI_ENDPOINT"]="Config.AZURE_OPENAI_API_ENDPOINT"
os.environ["AZURE_OPENAI_API_KEY"]=Config.AZURE_OPENAI_API_KEY
# os.environ['LANGSMITH_PROJECT']="Sonata-RAG-Management-System"
# os.environ['LANGSMITH_ENDPOINT'] ="https://api.smith.langchain.com" 
# os.environ["LANGCHAIN_TRACING_V2"] = "true"


class LLMService:
    def __init__(self, vector_store):
        self.llm = AzureChatOpenAI(
            temperature=0.7,
            azure_deployment="llm-gpt-4o",
            azure_endpoint=Config.AZURE_OPENAI_API_ENDPOINT,
            api_version="2024-08-01-preview"
        )
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.vector_store.as_retriever(),
            memory=self.memory
        )

    def get_response(self, query):
        try:
            response = self.chain.invoke({"question":query})
            return response['answer']
        except Exception as e:
            print(f"Error getting LLM response: {e}")
            return "I encountered an error processing your request."