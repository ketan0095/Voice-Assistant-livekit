from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import openai, deepgram, silero, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins.elevenlabs import TTS as ElevenLabsTTS
from config import config



llm = openai.LLM.with_azure(
        api_key=config.AZURE_OPENAI_KEY,
        api_version=config.AZURE_API_VERSION,
        azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
    )

def create_session() -> AgentSession:
    return AgentSession(
        stt=deepgram.STT(model=config.DEEPGRAM_MODEL, language="multi"),
        llm=llm,
        tts=ElevenLabsTTS(),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

def get_room_options() -> RoomInputOptions:
    return RoomInputOptions(
        noise_cancellation=noise_cancellation.BVC()
    )
