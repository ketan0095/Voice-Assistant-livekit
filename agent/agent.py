from logging import Logger
from livekit.agents import Agent,AgentSession

class Assistant(Agent):
    def __init__(self,session:AgentSession, logger:Logger,instructions:str) -> None:
        super().__init__(
            instructions=instructions
        )
        self._session = session
        self.logger =logger

    async def on_enter(self):
        # TODO: generate welcome msg here
        self._session.say("hello")
        self.logger.info("Agent entered room")

