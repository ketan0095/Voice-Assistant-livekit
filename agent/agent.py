"Base Voice Agent code."


from livekit.agents import Agent,AgentSession
from livekit.agents import function_tool, RunContext
from utils.types import CallContext
from utils.logger import VirtualAssistantLogger
from agent.agent_config import get_all_configs


class Assistant(Agent):
    """Initialize a custom agent with session context and logging."""
    def __init__(self,session:AgentSession, logger:VirtualAssistantLogger,
                instructions:str,
                call_context:CallContext) -> None:
        super().__init__(
            instructions=instructions
        )
        self._session = session
        self.logger =logger
        self.call_context =call_context
        self.agent_details = self.call_context.get("agent_details", {}).\
        get("agent_settings", {})

    async def on_enter(self):
        "Initialise agent speaking."
        welcome_msg = self.agent_details.get("welcome_settings", {}).\
        get("welcome_msg", {})  # noqa: E501
        if not welcome_msg:
            welcome_msg = get_all_configs().get("welcome_closing").get("welcome")
        self._session.say(welcome_msg)
        self.logger.debug("Agent has entered the room.")

    function_tool()
    async def end_call(self, ctx:RunContext):
        """Handle end of call msg."""
        self.logger.info(ctx)
        closing_msg = self.agent_details.get("closing_settings", {}).\
        get("closing_msg", {})  # noqa: E501
        if not closing_msg:
            closing_msg = get_all_configs().get("welcome_closing").get("clsoing")
        self._session.say(closing_msg)
        # delete room
        await ctx.delete_room()
