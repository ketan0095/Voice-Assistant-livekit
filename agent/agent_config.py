
"""Gather all agent config"""
from livekit.agents import Agent

DEFAULT_WELCOME_MSG ="Hello, how are you?"
DEFAULT_CLOSING_MSG ="Thank you, have a good day."


def get_all_configs():
    """Fetch all agent configs"""
    return {
        "welcome_closing":{
            "welcome":DEFAULT_WELCOME_MSG,
            "closing":DEFAULT_CLOSING_MSG
        }
    }

async def update_agent_tools(agent:Agent):
    """To dynamically update agent tools."""
    # TODO: Need to update tools as per requirements
    tools = list(agent.tools)
    await agent.update_tools(tools)
