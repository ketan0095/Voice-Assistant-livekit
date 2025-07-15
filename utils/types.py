"""Data classe for agent."""

from typing import Optional
from livekit.agents import JobContext

class CallContext:
    """
    Extended context wrapper around LiveKit JobContext to manage call-specific state.

    Attributes:
        job (JobContext): Original job context from LiveKit.
        org_info (dict): Organization metadata for prompt building.
        customer_name (Optional[str]): Known or extracted name of the caller.
        phone_number (Optional[str]): Phone number of the caller if available.
        language (str): Language preference for the call.
        transcription_provider (str): Backend used for speech-to-text.
        agent_name (str): Name of the voice agent handling this call.
    """

    def __init__(
        self,
        job: JobContext,
        org_info: dict,
        customer_name: Optional[str] = None,
        agent_number: Optional[str] = None,
        phone_number: Optional[str] = None,
        language: str = "en",
        transcription_provider: str = "deepgram",
        agent_name: Optional[str] = None,
        prompt: str =""
    ):
        self.job = job
        self.org_info = org_info
        self.customer_name = customer_name
        self.agent_number =agent_number
        self.phone_number = phone_number
        self.language = language
        self.transcription_provider = transcription_provider
        self.agent_name = agent_name
        self.prompt =prompt
