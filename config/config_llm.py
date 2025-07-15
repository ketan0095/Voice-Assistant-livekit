"Handle all llm configs for agent."

from livekit.plugins import openai, anthropic
from config.config import Config # pylint: disable=import-error
from utils.helper import require



# Azure OpenAI
def get_azure_openai_llm():
    """Return an Azure OpenAI LLM instance configured from environment."""
    return openai.LLM.with_azure(
        api_key=require(Config.AZURE_OPENAI_KEY, "AZURE_OPENAI_KEY"),
        api_version=require(Config.AZURE_API_VERSION, "AZURE_API_VERSION"),
        azure_endpoint=require(Config.AZURE_OPENAI_ENDPOINT, "AZURE_OPENAI_ENDPOINT"),
    )


# OpenAI
def get_openai_llm():
    """Return an OpenAI LLM instance configured from environment."""
    return openai.LLM(
        api_key=require(Config.OPENAI_API_KEY, "OPENAI_API_KEY"),
        model=require(Config.OPENAI_MODEL, "OPENAI_MODEL"),
    )


# Anthropic
def get_claude_llm():
    """Return an Anthropic Claude LLM instance configured from environment."""
    return anthropic.LLM(
        api_key=require(Config.ANTHROPIC_API_KEY, "ANTHROPIC_API_KEY"),
        model=require(Config.CLAUDE_MODEL, "CLAUDE_MODEL"),
    )
