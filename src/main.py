from conexao import supabase


# =========================================
# CADASTRAR PRODUTO
# =========================================
def cadastrar_produto():
    print("\n===== CADASTRAR PRODUTO =====")

    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        resposta_categorias = (
            supabase
            .table("categoria")
            .select("*")
            .execute()
        )

        categorias = resposta_categorias.data

        print("\nCategorias disponíveis:")

        for categoria in categorias:
            print(
                f"{categoria['id_categoria']} - "
                f"{categoria['nome']}"
            )

        id_categoria = int(
            input("\nDigite o ID da categoria: ")
        )

        dados = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "id_categoria": id_categoria
        }

        (
            supabase
            .table("produto")
            .insert(dados)
            .execute()
        )

        print("\nProduto cadastrado com sucesso!")

    except Exception as erro:
        print("\nErro ao cadastrar produto:")
        print(erro)


# =========================================
# LISTAR PRODUTOS
# =========================================
def listar_produtos():
    try:
        resposta = (
            supabase
            .table("produto")
            .select("*")
            .order("id_produto")
            .execute()
        )

        produtos = resposta.data

        print("\n===== PRODUTOS =====")

        if not produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in produtos:
            print("----------------------------")
            print(f"ID: {produto['id_produto']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Categoria: {produto['id_categoria']}")

    except Exception as erro:
        print("\nErro ao listar produtos:")
        print(erro)


# =========================================
# EDITAR PRODUTO
# =========================================
def editar_produto():
    print("\n===== EDITAR PRODUTO =====")

    try:
        listar_produtos()

        id_produto = int(
            input("\nDigite o ID do produto que deseja editar: ")
        )

        resposta = (
            supabase
            .table("produto")
            .select("*")
            .eq("id_produto", id_produto)
            .execute()
        )

        if not resposta.data:
            print("\nProduto não encontrado.")
            return

        novo_nome = input("Novo nome: ")
        novo_preco = float(
            input("Novo preço: R$ ")
        )

        dados = {
            "nome": novo_nome,
            "preco": novo_preco
        }

        (
            supabase
            .table("produto")
            .update(dados)
            .eq("id_produto", id_produto)
            .execute()
        )

        print("\nProduto atualizado com sucesso!")

    except Exception as erro:
        print("\nErro ao editar produto:")
        print(erro)


# =========================================
# EXCLUIR PRODUTO
# =========================================
def excluir_produto():
    print("\n===== EXCLUIR PRODUTO =====")

    try:
        listar_produtos()

        id_produto = int(
            input("\nDigite o ID do produto que deseja excluir: ")
        )

        resposta = (
            supabase
            .table("produto")
            .select("*")
            .eq("id_produto", id_produto)
            .execute()
        )

        if not resposta.data:
            print("\nProduto não encontrado.")
            return

        confirmar = input(
            "Tem certeza que deseja excluir? (s/n): "
        ).lower()

        if confirmar != "s":
            print("\nExclusão cancelada.")
            return

        (
            supabase
            .table("produto")
            .delete()
            .eq("id_produto", id_produto)
            .execute()
        )

        print("\nProduto excluído com sucesso!")

    except Exception as erro:
        print("\nErro ao excluir produto:")
        print(erro)


# =========================================
# VIEW
# RELATÓRIO DE ESTOQUE
# =========================================
def relatorio_estoque():
    print("\n===== RELATÓRIO DE ESTOQUE =====")

    try:
        resposta = (
            supabase
            .table("vw_relatorio_estoque")
            .select("*")
            .order("id_produto")
            .execute()
        )

        dados = resposta.data

        if not dados:
            print("Nenhum dado encontrado.")
            return

        for produto in dados:
            print("-------------------------------")
            print(f"ID: {produto['id_produto']}")
            print(f"Produto: {produto['produto']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Preço: R$ {produto['preco']}")
            print(f"Quantidade: {produto['quantidade']}")

            print(
                f"Valor em estoque: "
                f"R$ {produto['valor_em_estoque']}"
            )

            print(
                f"Situação: {produto['situacao']}"
            )

    except Exception as erro:
        print("\nErro ao consultar a View:")
        print(erro)


# =========================================
# FUNCTION
# CALCULAR VALOR EM ESTOQUE
# =========================================
def calcular_valor_estoque():
    print("\n===== CALCULAR VALOR DO ESTOQUE =====")

    try:
        listar_produtos()

        id_produto = int(
            input("\nDigite o ID do produto: ")
        )

        resposta_produto = (
            supabase
            .table("produto")
            .select("*")
            .eq("id_produto", id_produto)
            .execute()
        )

        if not resposta_produto.data:
            print("\nProduto não encontrado.")
            return

        produto = resposta_produto.data[0]

        resposta = (
            supabase
            .rpc(
                "calcular_valor_estoque",
                {
                    "p_id_produto": id_produto
                }
            )
            .execute()
        )

        print("\n===== RESULTADO =====")
        print(f"Produto: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']}")
        print(f"Quantidade: {produto['quantidade']}")

        print(
            f"Valor total em estoque: "
            f"R$ {resposta.data}"
        )

    except Exception as erro:
        print("\nErro ao executar a Function:")
        print(erro)


# =========================================
# PROCEDURE
# ENTRADA E SAÍDA DE ESTOQUE
# =========================================
def registrar_movimentacao(tipo):
    print(f"\n===== {tipo} DE ESTOQUE =====")

    try:
        listar_produtos()

        id_produto = int(
            input("\nDigite o ID do produto: ")
        )

        quantidade = int(
            input("Digite a quantidade: ")
        )

        resposta = (
            supabase
            .rpc(
                "executar_movimentacao_estoque",
                {
                    "p_id_produto": id_produto,
                    "p_quantidade": quantidade,
                    "p_tipo": tipo
                }
            )
            .execute()
        )

        print(f"\n{resposta.data}")

    except Exception as erro:
        print("\nErro ao executar a movimentação:")
        print(erro)


# =========================================
# HISTÓRICO DE MOVIMENTAÇÕES
# =========================================
def historico_movimentacoes():
    print("\n===== HISTÓRICO DE MOVIMENTAÇÕES =====")

    try:
        resposta = (
            supabase
            .table("movimentacao_estoque")
            .select("*")
            .order("data_movimentacao", desc=True)
            .execute()
        )

        movimentacoes = resposta.data

        print(
            f"\nQuantidade de movimentações encontradas: "
            f"{len(movimentacoes)}"
        )

        if not movimentacoes:
            print("Nenhuma movimentação registrada.")
            return

        for movimentacao in movimentacoes:
            print("--------------------------------")

            print(
                f"ID: {movimentacao['id_movimentacao']}"
            )

            print(
                f"Produto ID: {movimentacao['id_produto']}"
            )

            print(
                f"Tipo: {movimentacao['tipo']}"
            )

            print(
                f"Quantidade: {movimentacao['quantidade']}"
            )

            print(
                f"Data: {movimentacao['data_movimentacao']}"
            )

    except Exception as erro:
        print("\nERRO AO CONSULTAR HISTÓRICO:")
        print(erro)


# =========================================
# MENU PRINCIPAL
# =========================================
def menu():
    while True:

        print("""
=========================================
       SISTEMA DE CONTROLE DE ESTOQUE
=========================================

1 - Cadastrar produto
2 - Listar produtos
3 - Editar produto
4 - Excluir produto
5 - Relatório de estoque
    VIEW
6 - Calcular valor do estoque
    FUNCTION
7 - Registrar entrada
    PROCEDURE
8 - Registrar saída
    PROCEDURE
9 - Histórico de movimentações
0 - Sair

=========================================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            editar_produto()

        elif opcao == "4":
            excluir_produto()

        elif opcao == "5":
            relatorio_estoque()

        elif opcao == "6":
            calcular_valor_estoque()

        elif opcao == "7":
            registrar_movimentacao(
                "ENTRADA"
            )

        elif opcao == "8":
            registrar_movimentacao(
                "SAIDA"
            )

        elif opcao == "9":
            historico_movimentacoes()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida!")


# =========================================
# INICIAR PROGRAMA
# =========================================
if __name__ == "__main__":
    menu()