from redis_conexao import redis_client

try:
    print("Testando conexão com Redis...")

    print("PING:", redis_client.ping())

    redis_client.set("teste_integracao", "conectado", ex=60)

    print("Valor:", redis_client.get("teste_integracao"))

    print("Redis conectado com sucesso!")

except Exception as erro:
    print("Erro ao conectar ao Redis:", erro)