from logging import Logger
from livekit.agents import Agent,AgentSession

class Assistant(Agent):
    def __init__(self,session:AgentSession, logger:Logger) -> None:
        super().__init__(
            instructions="You are a helpful voice AI assistant."
        )
        self._session = session
        self.logger =logger

    async def on_enter(self):
        # TODO: generate welcome msg here
        self._session.say("hello")
        self.logger.info("Agent entered room")
        

