import openai
from config import Config
import tiktoken

# Configura tu clave de API de OpenAI
openai.api_key = Config.OPENAI_API_KEY
openai.api_base = Config.OPENAI_API_BASE
openai.api_type = Config.OPENAI_API_TYPE
openai.api_version = Config.OPENAI_API_VERSION

# Función para obtener la respuesta del modelo ChatGPT
deployment=Config.OPENAI_CHAT_DEPLOYMENT
def obtener_respuesta(conversacion):
    response = openai.ChatCompletion.create(
        engine=deployment,
        messages = conversacion,
        temperature=0.0,
        max_tokens=1000,
        stop=None
    )
    return response['choices'][0]['message']['content'].strip()

def num_tokens_from_string(string: str) -> int:
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens   

file = open("Correo.txt", "r", encoding = "utf-8")
mail = file.read()
file.close()

conversacion_actual = []
content = f"""
    Dado el contenido del siguiente email ''''{mail}'''', necesito que saques los siguientes datos de forma estructurada en formato JSON válido:
    Un ejemplo del objeto JSON de respuesta sería:
    ####
    Usuario que envia el mail: <nombre del usuario que envia el mail>,
    Usuario que recibe el mail: <nombre del usuario que recibe el mail>,
    Hora del envío: <fecha y hora del envío>,
    Subject: <asunto del mail>,
    Lista de tareas: [cada una de las tareas en formato texto dentro de este array]
    ####
    No añadas notas, ni información adicional. Solamente escribe el JSON.
    """

conversacion_actual.append({"role": "user", "content": content})
respuesta_chatbot = obtener_respuesta(conversacion_actual)
conversacion_actual.append({"role":"assistant","content":respuesta_chatbot})

print(respuesta_chatbot)
