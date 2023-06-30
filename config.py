import os

from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
SPOTIFY_CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
SPOTIFY_SECRET = os.environ.get('SPOTIFY_SECRET')
SPOTIFY_REDIRECT = 'http://localhost:3000'
DOCPATH = 'docs'
DOCDB = 'db/docs.chromadb'
