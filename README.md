
# Project Title

A brief description of what this project does and who it's for

# 🧠 LiveKit Voice Agent

A modular, real-time conversational voice agent built on top of [LiveKit Agents](https://docs.livekit.io/agents/), designed for natural, voice-based AI interaction over calls.  
This project provides a blueprint for building HIPAA-friendly voice assistants for scheduling, support, automation, and more.

---

## ⚙️ Features

- 🗣️ Voice-to-LLM real-time interaction  
- 🎙️ STT + TTS integration with Deepgram, ElevenLabs, etc.  
- 🧩 Modular prompt system with organization metadata  
- 📦 Session and agent context handling  
- 🧠 Multi-turn memory and dynamic prompt assembly  
- 🧾 Type-safe context injection and prompt templating  
- ✅ Ruff & Black compliant codebase  

---

## 🏗️ Project Structure

├── agent/ # LiveKit Agent entry points
│ ├── agent.py # Main agent logic
│ └── session.py # Handles session lifecycle & memory
│
├── config/ # Config management 
├── KMS/ # Key management / secrets (optional)
│
├── prompt_store/ # Prompt templates & rules
│ ├── global_rules.py # Global voice rules
│ ├── master_prompt.py # Persona + org prompt templates
│ └── prompt_builder.py # Assembles full prompt dynamically
│
├── utils/ # Utilities and support logic
│ ├── handler.py # Message handlers
│ ├── helper.py # Utility functions
│ ├── logger.py # Logging setup
│ └── types.py # Custom types like CallContext
│
├── main.py # Launch agent or service
├── .env # Environment variables (LiveKit keys, STT/TTS keys)
├── pyproject.toml # Dependencies, Ruff, Black etc.
└── README.md # You're here!

## 🚀 Quick Start

1. **Install dependencies using [uv](https://github.com/astral-sh/uv)**

```bash
uv venv         # Create a virtual environment (optional)
uv pip install -r requirements.txt
uv sync
```

2. **Create a .env file:**
Go through the .env.example for reference
```
# 🔐 LiveKit Credentials
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-livekit-server

# 🤖 LLM Provider
LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key

# 🗣️ Text-to-Speech (TTS)
TTS_PROVIDER=elevenlabs
ELEVENLABS_API_KEY=your_elevenlabs_api_key
TTS_VOICE_ID=your_voice_id

# 🎤 Speech-to-Text (STT)
STT_PROVIDER=deepgram
DEEPGRAM_API_KEY=your_deepgram_api_key

```

3. **Run the agent**

NOTE: If no done already, You must download the model weights before running your agent for the first time:
```
uv run main.py download-files
```
To run the agent:
```
uv run main.py dev
```

## 🧠 Prompt System
Prompts are built from reusable building blocks:

- global_rules.py: Common behavior like tone, fallback responses
- master_prompt.py: Persona template with dynamic org metadata
- prompt_builder.py: Generates prompt for full session

To customize your assistant for a new business:
```
org_info = {
  "company_name": "MediLink Health",
  "agent_goal": "help users book appointments",
  "trading_hours": "8 AM – 6 PM",
  "address": "123 Health Blvd",
  "service_types": "GP, Physio",
  "service_modalities": "in-person, telehealth"
}
```

## 📞 CallContext (Custom Context Wrapper)
CallContext (defined in types.py) extends JobContext from LiveKit with:

- Organization info for prompts
- Caller identity and preferences
- Language, STT/TTS provider
- Utility methods like get_prompt_context()

## 🧼 Code Quality
Add Ruff as a development dependency of your project:
```
uv add --dev ruff

## 📌 TODO

 - Add call history tracing
 - Context persistence across sessions
 - Integrate function-calling agents

```

## 📄 License

MIT © 2025 Ketan Krishna Shetye



