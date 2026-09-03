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

class Restaurantes(BaseModel):
    cidade:str = Field("A cidade recomendada para visitar")
    motivo:str = Field("Motivo pelo qual é interessante visitar essa cidade")

parseador_destino = JsonOutputParser(pydantic_object = Destino)
parseador_restaurante = JsonOutputParser(pydantic_object = Restaurantes)

prompt_cidade = PromptTemplate(
        template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador_destino.get_format_instructions()}
)

prompt_restaurante = PromptTemplate(
        template="""
    Sugira restaurantes populares entre locais em {cidade}.
    {formato_de_saida}
    """,
    partial_variables={"formato_de_saida": parseador_restaurante.get_format_instructions()}
)

prompt_cultural = PromptTemplate(
    template="Sugira atividades e locais culturais em {cidade}"
)

modelo = ChatOpenAI(
model="openai/gpt-oss-20b",
api_key=api_key,
base_url="https://api.groq.com/openai/v1"
)

cadeia1 = prompt_cidade | modelo | parseador_destino
cadeia2 = prompt_restaurante | modelo | parseador_restaurante
cadeia3 = prompt_cultural | modelo | StrOutputParser()

cadeia = (cadeia1 | cadeia2 | cadeia3)

resposta = cadeia.invoke({
    "interesse" : "praias"
})

print(resposta)