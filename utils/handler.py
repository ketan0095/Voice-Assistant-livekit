
from livekit.agents import AgentSession,MetricsCollectedEvent,UserStateChangedEvent,AgentStateChangedEvent


def speech_handler(session:AgentSession):


    @session.on("conversation_item_added")
    def on_conversation_item_added(item):
        #TODO: Save conversation history here            
        ...

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        #TODO: Save STT,LLM,TTS,EOU metrics here
        ...
    
    @session.on("function_tools_executed")
    def _on_function_tools_executed(ev):
        #TODO: get function execution details here
        ...

def handle_inactivity(session: AgentSession):
    #TODO: Handle user inactivity here
    
    @session.on("user_state_changed")
    def on_user_state_changed(ev: UserStateChangedEvent):
        #TODO: Track user activity here
        ...

    @session.on("agent_state_changed")
    def on_agent_state_changed(ev: AgentStateChangedEvent):
        #TODO: Track assistant activity here
        ...