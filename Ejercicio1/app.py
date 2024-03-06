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

while True:
    content = input("User ('salir' para terminar): ")

    if content == "salir":
        break

    conversation.append({
        "role": "user", "content": content
    })

    response = openai.ChatCompletion.create(
        engine = deployment,
        messages = conversation,
        temperature = 0.7,
        max_tokens=150,
        stop=None
    )

    message = response["choices"][0]["message"]["content"]
    
    print("Chatbot: " + message)
    print("Tokens: " + str(num_tokens_from_string(message, "cl100k_base")))

    conversation.append({
        "role": "assistant", "content": message
    })
