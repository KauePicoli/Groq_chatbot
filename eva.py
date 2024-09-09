import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
chave_api = os.getenv("GROQ_API_KEY")

modelo = ChatGroq(model="llama3-8b-8192")
parser = StrOutputParser()

template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "seu nome é EVA e você responde as perguntas em portugues de forma simples e curta"),
    ("user", "{texto}")
])

chain = template_mensagem | modelo | parser

while True:
    texto_usuario = input("Você: ")
    if texto_usuario.lower() in ["sair"]:
        break
    resposta = chain.invoke({"texto": texto_usuario})
    print(f"EVA: {resposta}")