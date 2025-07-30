import requests
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HEADER_TOKEN")

url = "https://webhook.syscoin.com.br/webhook/teste-estagio"

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

body = {
    "Name": "Matheus Costa Gomes",
    "Response": "Possuo conhecimento na área de desenvolvimento, \
sou organizado, disciplinado e sempre interessado em \
aprender mais, crescer e em contribuir com aquilo que sei para \
poder fazer a diferença, além de que acredito que tenho o perfil buscado \
e que posso agregar ao crescimento da empresa."
}


response = requests.post(url, json=body, headers=headers)

print(response.status_code)
print(response.text)

