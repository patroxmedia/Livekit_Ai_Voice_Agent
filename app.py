from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent, inference, room_io, TurnHandlingOptions
from livekit.plugins import ai_coustics, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins import google
from livekit.plugins import sarvam
# from livekit.plugins import openai




load_dotenv(".env")

SYSTEM_PROMPT = """
You are Priya, a Hindi voice assistant.

IMPORTANT RULES:
- Always reply in Hindi written in Devanagari script.
- Never reply in English unless the user explicitly asks for English.
- Keep responses short and conversational.
- Speak naturally like a customer support agent.
- Introduce yourself as Priya.
- Do not use markdown or special characters.

Examples:
User: Hello
Assistant: नमस्ते, मैं प्रिया हूँ। मैं आपकी कैसे सहायता कर सकती हूँ?

User: How are you?
Assistant: मैं ठीक हूँ। आप कैसे हैं?
"""

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=SYSTEM_PROMPT,
        )

server = AgentServer()

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: agents.JobContext):
    session = AgentSession(
        # stt=inference.STT(model="deepgram/nova-3", language="multi"),
        # Saaras v3 STT - Converts speech to text
            stt=sarvam.STT(
                language="hi-IN",  # Auto-detect language, or use "en-IN", "hi-IN", etc.
                model="saaras:v3",
                mode="transcribe"
            ),

        # llm=openai.LLM.with_ollama(model="gemma:2b", base_url="http://localhost:11434/v1",),
        llm=inference.LLM(model="google/gemini-2.5-flash-lite"),
        # tts=inference.TTS(
        #     model="cartesia/sonic-3.5",
        #     voice="65209f8e-6140-4a20-b819-3cc2e21da19b",
        # ),

        # Bulbul TTS - Converts text to speech
            tts=sarvam.TTS(
                target_language_code="hi-IN",
                
                model="bulbul:v3",
                speaker="simran", # Female: priya, simran, ishita, kavya | Male: aditya, anand, rohan
                
            ),

        vad=silero.VAD.load(),
        turn_handling=TurnHandlingOptions(
            turn_detection=MultilingualModel(),
        ),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=ai_coustics.audio_enhancement(model=ai_coustics.EnhancerModel.QUAIL_VF_S),
            ),
        ),
    )

    await session.generate_reply(
        instructions="""
            Greet the user warmly in Hindi.
            Introduce yourself as Priya.
            Ask how you can help.
            Keep it under 15 words.
            Say exactly:
            'नमस्ते! मैं प्रिया हूँ। मैं आपकी कैसे सहायता कर सकती हूँ?'

         """
            
    )


if __name__ == "__main__":
    agents.cli.run_app(server)