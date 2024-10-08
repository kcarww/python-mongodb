from dotenv import load_dotenv
import os
from pymongo import MongoClient
from urllib.parse import quote_plus


load_dotenv()
password = quote_plus(os.getenv("SENHA"))


connection_string = f"mongodb+srv://carl:{password}@cluster0.byzne.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection_string)
db = client.test
# print("Conectado com sucesso:", db)

db = client['escola']
collection = db['alunos']
# print(db)
# print(collection)


def inserir():
    documento = {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo"
    }

    result = collection.insert_one(documento)
    print(f"Documento inserido com id: {result.inserted_id}")


def buscar():
    resultados = collection.find()
    for documento in resultados:
        print(documento)


def update_one():
    filtro = {"nome": "João"}
    novo_valor = {"$set": {"idade": 31, "nome": "Jones"}}

    collection.update_one(filtro, novo_valor)
    print(f"Documento atualizado.")


def deletar():
    filtro = {"nome": "João"}
    collection.delete_one(filtro)
    print(f"Documento deletado.")


def deletar_varios():
    filtro = {"cidade": "Rio de Janeiro"}
    collection.delete_many(filtro)
    print(f"Documentos deletados.")


def operadores():
    filtro = {
        "$or": [
            {"idade": {"$gt": 20}},
            {"cidade": "São Paulo"}
        ]
    }

    resultados = collection.find(filtro)

    for aluno in resultados:
        print(aluno)
