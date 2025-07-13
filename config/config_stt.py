from livekit.plugins import deepgram, whisper, azure, google, assemblyai
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
    return whisper.STT.with_openai_api(
        api_key=require(Config.OPENAI_API_KEY, "OPENAI_API_KEY"),
        model=require(Config.WHISPER_API_MODEL, "WHISPER_API_MODEL"),
        language=getattr(Config, "WHISPER_API_LANGUAGE", "en"),
    )

# Whisper.cpp 
def get_whisper_cpp_stt():
    return whisper.STT.with_whisper_cpp(
        model_path=require(Config.WHISPER_CPP_MODEL_PATH, "WHISPER_CPP_MODEL_PATH"),
        language=getattr(Config, "WHISPER_CPP_LANGUAGE", "en"),
    )

# Azure Speech
def get_azure_stt():
    return azure.STT(
        api_key=require(Config.AZURE_SPEECH_KEY, "AZURE_SPEECH_KEY"),
        region=require(Config.AZURE_SPEECH_REGION, "AZURE_SPEECH_REGION"),
        language=getattr(Config, "AZURE_SPEECH_LANGUAGE", "en-US"),
    )

# Google Cloud STT
def get_google_stt():
    return google.STT(
        credentials=require(Config.GOOGLE_CLOUD_CREDENTIALS_JSON, "GOOGLE_CLOUD_CREDENTIALS_JSON"),
        language=getattr(Config, "GOOGLE_SPEECH_LANGUAGE", "en-US"),
    )

# AssemblyAI
def get_assemblyai_stt():
    return assemblyai.STT(
        api_key=require(Config.ASSEMBLYAI_API_KEY, "ASSEMBLYAI_API_KEY"),
        model=getattr(Config, "ASSEMBLYAI_MODEL", None),
        language=getattr(Config, "ASSEMBLYAI_LANGUAGE", "en"),
    )
