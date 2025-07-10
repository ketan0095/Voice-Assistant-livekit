from config import config
from livekit.plugins import openai

def get_llm_config():
   return openai.LLM.with_azure(
            api_key=config.AZURE_OPENAI_KEY,
            api_version=config.AZURE_API_VERSION,
            azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
        )