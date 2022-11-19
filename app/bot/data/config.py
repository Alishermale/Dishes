# there are all parameters from .env file
import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
admin_id = os.getenv('ADMIN_ID')
