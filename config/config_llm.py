from config.config import Config
from livekit.plugins import openai

def get_llm_config():
   return openai.LLM.with_azure(
            api_key=Config.AZURE_OPENAI_KEY,
            api_version=Config.AZURE_API_VERSION,
            azure_endpoint=Config.AZURE_OPENAI_ENDPOINT,
        )