import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

modelo = ChatOpenAI(
model="openai/gpt-oss-20b",
api_key=api_key,
base_url="https://api.groq.com/openai/v1"
)

lista_perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e cultura. Pode sugerir?",
    "Qual a melhor época do ano para ir?"
]

for uma_pergunta in lista_perguntas:
    resposta = modelo.invoke(uma_pergunta)
    print("Usuário: ", uma_pergunta)
    print("IA: ", resposta.content, "\n")