"Base Voice Agent code."

from logging import Logger
from livekit.agents import Agent,AgentSession

class Assistant(Agent):
    """Initialize a custom agent with session context and logging."""
    def __init__(self,session:AgentSession, logger:Logger,instructions:str) -> None:
        super().__init__(
            instructions=instructions
        )
        self._session = session
        self.logger =logger

    async def on_enter(self):
        "Initialise agent speaking."
        # TODO: generate welcome msg here
        self._session.say("hello")
        self.logger.info("Agent entered room")
