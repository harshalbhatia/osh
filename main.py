import os
import openai
from models import models
from dotenv import load_dotenv
load_dotenv()

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")

CURRENT_MODEL = models.get(os.getenv("CURRENT_MODEL"))
DEPLOYMENT_ID = os.getenv("DEPLOYMENT_ID")

def callCurrentModelWithData(data):
    # figure out currently configured model
    # calls it in a generic manner
    # returns the result
