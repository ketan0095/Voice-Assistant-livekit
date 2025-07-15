"""Data classe for agent."""

from typing import Optional
from dataclasses import dataclass
from livekit.agents import JobContext

# pylint: disable=too-many-instance-attributes
@dataclass
class CallContext:
    """
    Extended context wrapper around LiveKit JobContext to manage call-specific state.

    Attributes:
        job (JobContext): Original job context from LiveKit.
        org_info (dict): Organization metadata for prompt building.
        customer_name (Optional[str]): Known or extracted name of the caller.
        agent_number (Optional[str]): Identifier for the voice agent.
        phone_number (Optional[str]): Phone number of the caller if available.
        language (str): Language preference for the call.
        transcription_provider (str): Backend used for speech-to-text.
        agent_name (Optional[str]): Name of the voice agent handling this call.
        prompt (str): The dynamic or static prompt used during the call.
    """
    job: 'JobContext'  # use forward reference if JobContext is not imported yet
    org_info: dict
    customer_name: Optional[str] = None
    agent_number: Optional[str] = None
    phone_number: Optional[str] = None
    language: str = "en"
    transcription_provider: str = "deepgram"
    agent_name: Optional[str] = None
    prompt: str = ""
