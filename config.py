import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
APP_HOST = os.getenv("APP_HOST", "127.0.0.1").strip()
APP_PORT = int(os.getenv("APP_PORT", "8000"))
