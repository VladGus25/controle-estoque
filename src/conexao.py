from supabase import create_client, Client
from dotenv import load_dotenv
from pathlib import Path
import os

# Localiza o arquivo .env na pasta principal do projeto
caminho_env = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=caminho_env)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL não foi encontrada no arquivo .env")

if not SUPABASE_KEY:
    raise ValueError("SUPABASE_KEY não foi encontrada no arquivo .env")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)