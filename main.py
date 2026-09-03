from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain.globals import set_debug
from pydantic import Field, BaseModel

set_debug(True)
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

class Destino(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    motivo:str = Field("Motivo pelo qual é interessante visitar essa cidade")

parseador = JsonOutputParser(pydantic_object = Destino)

prompt_cidade = PromptTemplate(
        template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador.get_format_instructions()}
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

print(resposta)