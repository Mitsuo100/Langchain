from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

import os

from langchain.prompts import PromptTemplate

load_dotenv()

from langchain_core.output_parsers import StrOutputParser

api_key = os.getenv("GROQ_API_KEY")

prompt_cidade = PromptTemplate(
        template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    """,
    input_variables=["interesse"]
)

modelo = ChatOpenAI(
model="openai/gpt-oss-20b",
api_key=api_key,
base_url="https://api.groq.com/openai/v1"
)

cadeia = prompt_cidade | modelo | StrOutputParser()

resposta = cadeia.invoke({
    "interesse" : "praias"
})

print(resposta.content)