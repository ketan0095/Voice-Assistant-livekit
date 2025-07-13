from livekit.plugins import deepgram,openai,google
from livekit.plugins.azure import stt
from config.config import Config
from utils.helper import require

# Deepgram
def get_deepgram_stt():
    return deepgram.STT(
        api_key=require(Config.DEEPGRAM_API_KEY, "DEEPGRAM_API_KEY"),
        model=require(Config.DEEPGRAM_MODEL, "DEEPGRAM_MODEL"),
        language=getattr(Config, "DEEPGRAM_LANGUAGE", "en"),  # optional
    )

# OpenAI Whisper
def get_whisper_api_stt():
    return openai.STT.with_openai_api(
    api_key=Config.OPENAI_API_KEY,
    model=Config.WHISPER_API_MODEL,  # e.g., "whisper-1"
    language=Config.WHISPER_API_LANGUAGE,
)

# Whisper.cpp 
def get_whisper_cpp_stt():
    return openai.STT.with_whisper_cpp(
    model_path=Config.WHISPER_CPP_MODEL_PATH,  # e.g., "./models/ggml-base.en.bin"
    language=Config.WHISPER_CPP_LANGUAGE,
)

# Azure Speech
def get_azure_stt():
    return stt.STT(
        speech_key=require(Config.AZURE_SPEECH_KEY, "AZURE_SPEECH_KEY"),
        speech_region=require(Config.AZURE_SPEECH_REGION, "AZURE_SPEECH_REGION"),
        language=getattr(Config, "AZURE_SPEECH_LANGUAGE", "en-US"),
        # Optionally add speech_host if needed
        speech_host=Config.AZURE_SPEECH_HOST,  # optional override
    )

# Google Cloud STT
def get_google_stt():
    return google.STT(
        credentials=require(Config.GOOGLE_CLOUD_CREDENTIALS_JSON, "GOOGLE_CLOUD_CREDENTIALS_JSON"),
        language=getattr(Config, "GOOGLE_SPEECH_LANGUAGE", "en-US"),
    )


