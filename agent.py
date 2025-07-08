from livekit.agents import AgentWorker, AgentSession
from livekit.agents.llm import ChatOpenAI
from livekit.agents.stt import DeepgramSTT
from livekit.agents.tts import ElevenLabsTTS
from livekit.agents.text import TextAgent
from livekit.agents.voice import VoiceAgent

from config import settings
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def create_agent():
    # LLM
    llm = ChatOpenAI(api_key=settings.OPENAI_API_KEY)

    # Text-only agent
    base_agent = TextAgent(
        llm=llm,
        system_prompt="You are a helpful assistant.",
    )

    if settings.ENABLE_AUDIO:
        # Add voice layer
        stt = DeepgramSTT(api_key=settings.DEEPGRAM_API_KEY)
        tts = ElevenLabsTTS(api_key=settings.ELEVENLABS_API_KEY, voice=settings.VOICE_ID)
        agent = VoiceAgent(text_agent=base_agent, stt=stt, tts=tts)
    else:
        agent = base_agent

    return agent


class MyWorker(AgentWorker):
    async def on_session_start(self, session: AgentSession):
        logger.info(f"Session started for {session.agent_info.name}")

        await session.say("Hello! I'm your test agent.", allow_interruptions=True)

    async def on_session_end(self, session: AgentSession):
        logger.info("Session ended.")

    async def on_message(self, session: AgentSession, message: str):
        logger.info(f"User said: {message}")
