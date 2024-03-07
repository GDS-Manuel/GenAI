from dotenv import load_dotenv
import os
load_dotenv()
 
class Config:
    AZURE_STORAGE_ACCOUNT=os.environ.get("AZURE_STORAGE_ACCOUNT")
    AZURE_STORAGE_KEY=os.environ.get("AZURE_STORAGE_KEY")
    AZURE_STORAGE_USER_TABLE=os.environ.get("AZURE_STORAGE_USER_TABLE")
    AZURE_ENDPOINT_TEST=os.environ.get("AZURE_ENDPOINT_TEST")