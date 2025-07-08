from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import openai, deepgram, silero, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins.elevenlabs import TTS as ElevenLabsTTS
from livekit.plugins.openai import LLM
from config import config
from openai import AzureOpenAI

print("config :",config.AZURE_OPENAI_ENDPOINT)

client = AzureOpenAI(
    azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
    api_key=config.AZURE_OPENAI_KEY,
    api_version="2024-02-15-preview"
)

llm = LLM(
    model="gpt-4",  # NOT "gpt-4", use the deployment name
    client=client
)

def create_session() -> AgentSession:
    return AgentSession(
        stt=deepgram.STT(model=config.DEEPGRAM_MODEL, language="multi"),
        llm=openai.LLM(model=config.OPENAI_MODEL),
        tts=ElevenLabsTTS(),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

def get_room_options() -> RoomInputOptions:
    return RoomInputOptions(
        noise_cancellation=noise_cancellation.BVC()
    )
