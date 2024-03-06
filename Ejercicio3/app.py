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

def prompt_context(context):
    return f"""
        Eres un asistente encargado de identificar si la pregunta del usuario esta relacionada con el historial de chat.
        En caso de ser una pregunta relacionada, debes responder unicamente con la palabra "true".
        Si no esta relacionada, debes responder unicamente con la palabra "false".
        A continuación, tienes el historial de chat para que compares con  la pregunta del usuario
        Historial de chat: ````{context}''''
        """

print("Bienvenido al Chatbot. Puedes salir en cualquier momento escribiendo 'salir'.")
conversacion_actual = []
conversacion_actual.append({"role": "system", "content": "You are a helpful assistant."})

while True:
    usuario_input = input("Usuario: ")
    print("Tokens: ",num_tokens_from_string(usuario_input))
    if usuario_input.lower() == 'salir':
        print("Hasta luego. ¡Que tengas un buen día!")
        break
    contexto=[]
    conversacion_actual.append({"role":"user","content":usuario_input})
    #Ejercicio para resetear los contextos 
    if len(conversacion_actual) >= 3:
        system_content = prompt_context(conversacion_actual) #Obtengo el prompt del system con el historial de conversacion
        contexto.append({"role": "system", "content": system_content}) #me creo un array de conversacion para enviarselo a gpt
        contexto.append({"role":"user", "content": usuario_input}) #Añado la pregunta a este array con el role user
        response = obtener_respuesta(contexto) #Obtengo respuesta
        print(response)
        if(response == "false"): 
            conversacion_actual = []
            conversacion_actual.append({"role": "system", "content": "You are a helpful assistant."})
            conversacion_actual.append({"role":"user", "content": usuario_input})
    print(conversacion_actual)
    # Agregar el nuevo mensaje del usuario a la conversación
    # Obtener la respuesta del chatbot y agregarla a la conversación
    respuesta_chatbot = obtener_respuesta(conversacion_actual)
    conversacion_actual.append({"role":"assistant","content":respuesta_chatbot})
    # Mostrar la respuesta del chatbot
    print("Chatbot:", respuesta_chatbot)





# prompt_context = """I need your assistance in evaluating whether a given context is necessary for a given input.
#         Your task is to analyze the relationship between the context and the input, and determine if the context is essential for understanding or interpreting the input.
#         If the context is necessary, please respond with "True". If the context is not necessary, please respond with "False".
#         Here are a few examples to guide you:
#         ####
#         Input: "Hasta cuando puedo contratarla?"
#         Context: "['user': 'Dime la promocion de Netflix', 'assistant': ' ((False)) La promoción de Netflix ofrece un descuento del 25% durante 3 meses en el paquete Netflix Estándar/X2 y Premium/X4 con IPTV para nuevos clientes Fusión o miMovistar. También hay un descuento del 50% durante 3 meses si se contratan estos paquetes con un dispositivo de una selección. Tenga en cuenta que esta promoción no es compatible con clientes que ya tengan esos paquetes contratados o productos que incluyan esos servicios. Si el cliente se da de baja de la oferta con Netflix, perderá la promoción de Motor. ((False))']"
#         Output: "True"
#         ###
#         IMPORTANT! Don't add any explanation, comments or notes about your response."""