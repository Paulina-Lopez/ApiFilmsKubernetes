from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_SERVICE = os.getenv('POSTGRES_SERVICE', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

# Database configuration
SQLALCHEMY_DATABASE_URI =os.environ.get('DATABASE_URL','sqlite:///films.sqlite',f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVICE}:{POSTGRES_PORT}/{POSTGRES_DB}')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

ERROR_404_HELP = False
