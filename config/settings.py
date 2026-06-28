import os
from dotenv import load_dotenv

load_dotenv()

CIRCLE_API_KEY = os.getenv("CIRCLE_API_KEY")
CIRCLE_ENTITY_SECRET = os.getenv("CIRCLE_ENTITY_SECRET")
