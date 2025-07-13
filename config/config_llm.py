from config.config import Config
from livekit.plugins import openai, anthropic, ollama, togetherai, mistral, cohere


def require(value, name: str):
    if not value:
        raise ValueError(f"Missing required config value: {name}")
    return value

# Azure OpenAI
def get_azure_openai_llm():
    return openai.LLM.with_azure(
        api_key=require(Config.AZURE_OPENAI_KEY, "AZURE_OPENAI_KEY"),
        api_version=require(Config.AZURE_API_VERSION, "AZURE_API_VERSION"),
        azure_endpoint=require(Config.AZURE_OPENAI_ENDPOINT, "AZURE_OPENAI_ENDPOINT"),
        deployment_name=require(Config.AZURE_DEPLOYMENT_NAME, "AZURE_DEPLOYMENT_NAME"),
    )


# OpenAI
def get_openai_llm():
    return openai.LLM.with_openai(
        api_key=require(Config.OPENAI_API_KEY, "OPENAI_API_KEY"),
        model=require(Config.OPENAI_MODEL, "OPENAI_MODEL"),
    )

# Anthropic
def get_claude_llm():
    return anthropic.LLM.with_anthropic(
        api_key=require(Config.ANTHROPIC_API_KEY, "ANTHROPIC_API_KEY"),
        model=require(Config.CLAUDE_MODEL, "CLAUDE_MODEL"),
    )


# Mistral
def get_mistral_llm():
    return mistral.LLM.with_mistral(
        api_key=require(Config.MISTRAL_API_KEY, "MISTRAL_API_KEY"),
        model=require(Config.MISTRAL_MODEL, "MISTRAL_MODEL"),
    )

# Together.ai
def get_togetherai_llm():
    return togetherai.LLM.with_togetherai(
        api_key=require(Config.TOGETHER_API_KEY, "TOGETHER_API_KEY"),
        model=require(Config.TOGETHER_MODEL, "TOGETHER_MODEL"),
    )


# Cohere
def get_cohere_llm():
    return cohere.LLM.with_cohere(
        api_key=require(Config.COHERE_API_KEY, "COHERE_API_KEY"),
        model=require(Config.COHERE_MODEL, "COHERE_MODEL"),
    )


# Ollama (local model)
def get_ollama_llm():
    return ollama.LLM.with_ollama(
        model=require(Config.OLLAMA_MODEL, "OLLAMA_MODEL"),
        endpoint=getattr(Config, "OLLAMA_HOST", None),  # optional
    )