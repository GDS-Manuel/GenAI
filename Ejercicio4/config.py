from dotenv import load_dotenv
import os
load_dotenv()
 
class Config:
    OPENAI_API_BASE=os.environ.get("OPENAI_API_BASE")
    OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
    OPENAI_API_VERSION=os.environ.get("OPENAI_API_VERSION")
    OPENAI_API_TYPE=os.environ.get("OPENAI_API_TYPE")
    OPENAI_CHAT_DEPLOYMENT=os.environ.get("OPENAI_CHAT_DEPLOYMENT")