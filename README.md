# LiveKit AI Voice Agent

A real-time AI Voice Agent built using Python, LiveKit, and Large Language Models (LLMs). The agent can listen to user speech, understand intent, generate intelligent responses, and reply with natural-sounding voice.

## Features

* Real-time voice conversations
* Speech-to-Text (STT)
* Large Language Model (LLM) integration
* Text-to-Speech (TTS)
* Turn detection and interruption handling
* Multi-language support
* WebRTC-based communication using LiveKit
* Extensible tool/function calling
* Session memory and context management

## Tech Stack

* Python 3.11+
* LiveKit Agents
* OpenAI / Gemini / Anthropic
* Sarvam AI / Deepgram / Whisper
* FastAPI
* WebRTC
* WebSockets
* Docker

## Project Structure

```text
ai-voice-agent/
├── frontend
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── logs/
```

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd Livekit_Ai_Voice_Agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
LIVEKIT_URL=
LIVEKIT_API_KEY=
LIVEKIT_API_SECRET=

OPENAI_API_KEY=
GOOGLE_API_KEY=
SARVAM_API_KEY=
```

### 5. Run Agent

```bash
python agent.py dev
```

## LiveKit Installation

Install LiveKit Agents:

```bash
pip install livekit-agents
```

Install common plugins:

```bash
pip install livekit-plugins-openai
pip install livekit-plugins-sarvam
pip install livekit-plugins-silero
```

Or install everything together:

```bash
pip install livekit-agents livekit-plugins-openai livekit-plugins-sarvam livekit-plugins-silero
```

## Running in Development

```bash
python app.py dev
```

## Running in Frontend Development

```bash
npm run dev
```

## Example Workflow

User Speaks
↓
Speech-to-Text
↓
LLM Processing
↓
Tool Calling (Optional)
↓
Text Generation
↓
Text-to-Speech
↓
Voice Response

## License

MIT License
