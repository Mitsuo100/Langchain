from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

modelo = ChatOpenAI(
model="openai/gpt-oss-20b",
api_key=api_key,
base_url="https://api.groq.com/openai/v1"
)

prompt_consultor = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um consultor de viagens"),
        ("human", "{query}")
    ]
)

assistente = prompt_consultor | modelo | StrOutputParser()

print(assistente.invoke({"query": "Quero férias em praias no Brasil."}))