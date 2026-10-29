import os
import redis
from dotenv import load_dotenv
from pathlib import Path

# Carrega o .env da pasta principal
caminho_env = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=caminho_env)

# Conexão com Redis
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    username=os.getenv("REDIS_USERNAME", "default"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
    ssl=False,
    socket_connect_timeout=5,
    socket_timeout=5,
    protocol=2
)


def obter_cache(chave):
    try:
        return redis_client.get(chave)
    except redis.RedisError as erro:
        print(f"\nAviso: Redis indisponível: {erro}")
        return None


def salvar_cache(chave, valor, tempo=300):
    try:
        redis_client.setex(chave, tempo, valor)
    except redis.RedisError as erro:
        print(f"\nAviso: não foi possível salvar no Redis: {erro}")


def limpar_cache_produtos():
    try:
        redis_client.delete("produtos")
        print("[REDIS] Cache de produtos atualizado.")
    except redis.RedisError as erro:
        print(f"\nAviso: não foi possível limpar o cache: {erro}")