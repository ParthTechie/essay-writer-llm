import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API settings
GROQ_API_KEY = os.environ.get("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")
DEFAULT_MODEL = "llama3-70b-8192"
DEFAULT_MAX_TOKENS = 4000
DEFAULT_TEMPERATURE = 0.7