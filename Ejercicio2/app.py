import openai, tiktoken
from config import Config

openai.api_base    = Config.OPENAI_API_BASE
openai.api_key     = Config.OPENAI_API_KEY
openai.api_type    = Config.OPENAI_API_TYPE
openai.api_version = Config.OPENAI_API_VERSION
deployment         = Config.OPENAI_CHAT_DEPLOYMENT
conversation       = []

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding   = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens  

file = open("data.txt", "r", encoding = "utf-8")
data = file.read()
file.close()

content = "Dado el siguiente contenido '" + data + "', necesito extraer la siguiente información: Nombre de arrendador, DNI de arrendador, Nombre de arrendatario, DNI de Arrendatario, Duración del contrato, Dirección del domicilio a arrendar"

conversation.append({
    "role": "user", "content": content
})

response = openai.ChatCompletion.create(
    engine = deployment,
    messages = conversation,
    temperature = 0.7,
    max_tokens=1000,
    stop=None
)

message = response["choices"][0]["message"]["content"]

print(message)
print("Tokens: " + str(num_tokens_from_string(message, "cl100k_base")))
