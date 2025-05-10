# 📌 main.py — FastAPI + MCPServer + Twilio Webhook Integration

from fastapi import FastAPI, Request
from mcpserver import MCPServer
from llm_utils import generate_reply
import os
from dotenv import load_dotenv

load_dotenv()

# 🔧 Initialize MCPServer and FastAPI
app = FastAPI()
server = MCPServer(app)

# 📩 Twilio webhook endpoint to receive WhatsApp messages
@server.route("/webhook", methods=["POST"])
async def whatsapp_webhook(request: Request):
    form = await request.form()
    sender = form.get("From")
    message_body = form.get("Body")

    print(f"📥 Message from {sender}: {message_body}")

    # 🤖 Generate a friendly reply using OpenAI LLM
    reply_text = await generate_reply(message_body)

    # 📤 Send reply back (Twilio call would be added here)
    print(f"📤 Reply to {sender}: {reply_text}")

    return {"status": "ok"}
