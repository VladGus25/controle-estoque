import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from conexao import supabase
from redis_conexao import obter_cache, salvar_cache, limpar_cache_produtos
import json

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "controle-estoque-secret")


# ─────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────
@app.route("/")
def dashboard():
    try:
        # Total de produtos
        resp_produtos = supabase.table("produto").select("*").execute()
        produtos = resp_produtos.data or []

        # Relatório (view)
        resp_relatorio = (
            supabase.table("vw_relatorio_estoque")
            .select("*")
            .execute()
        )
        relatorio = resp_relatorio.data or []

        total_produtos = len(produtos)
        sem_estoque = sum(1 for p in relatorio if p.get("situacao") == "Sem estoque")
        estoque_baixo = sum(1 for p in relatorio if p.get("situacao") == "Estoque baixo")
        valor_total = sum(float(p.get("valor_em_estoque") or 0) for p in relatorio)

        # Últimas movimentações
        resp_mov = (
            supabase.table("movimentacao_estoque")
            .select("*")
            .order("data_movimentacao", desc=True)
            .limit(5)
            .execute()
        )
        movimentacoes = resp_mov.data or []

        return render_template(
            "dashboard.html",
            total_produtos=total_produtos,
            sem_estoque=sem_estoque,
            estoque_baixo=estoque_baixo,
            valor_total=valor_total,
            movimentacoes=movimentacoes,
            relatorio=relatorio[:5]
        )
    except Exception as e:
        flash(f"Erro ao carregar dashboard: {e}", "erro")
        return render_template("dashboard.html",
            total_produtos=0, sem_estoque=0,
            estoque_baixo=0, valor_total=0,
            movimentacoes=[], relatorio=[])


# ─────────────────────────────────────────
# PRODUTOS — LISTAR
# ─────────────────────────────────────────
@app.route("/produtos")
def listar_produtos():
    try:
        cache_origem = None
        produtos_cache = obter_cache("produtos")

        if produtos_cache:
            produtos = json.loads(produtos_cache)
            cache_origem = "redis"
        else:
            resp = (
                supabase.table("produto")
                .select("*, categoria(nome)")
                .order("id_produto")
                .execute()
            )
            produtos = resp.data or []
            salvar_cache("produtos", json.dumps(produtos), 300)
            cache_origem = "supabase"

        return render_template("produtos.html",
                               produtos=produtos,
                               cache_origem=cache_origem)
    except Exception as e:
        flash(f"Erro ao listar produtos: {e}", "erro")
        return render_template("produtos.html", produtos=[], cache_origem=None)


# ─────────────────────────────────────────
# PRODUTOS — CADASTRAR
# ─────────────────────────────────────────
@app.route("/produtos/novo", methods=["GET", "POST"])
def cadastrar_produto():
    if request.method == "POST":
        try:
            dados = {
                "nome": request.form["nome"],
                "preco": float(request.form["preco"]),
                "quantidade": int(request.form["quantidade"]),
                "id_categoria": int(request.form["id_categoria"])
            }
            supabase.table("produto").insert(dados).execute()
            limpar_cache_produtos()
            flash("Produto cadastrado com sucesso!", "sucesso")
            return redirect(url_for("listar_produtos"))
        except Exception as e:
            flash(f"Erro ao cadastrar produto: {e}", "erro")

    try:
        resp = supabase.table("categoria").select("*").execute()
        categorias = resp.data or []
    except Exception as e:
        categorias = []
        flash(f"Erro ao carregar categorias: {e}", "erro")

    return render_template("produto_form.html", produto=None, categorias=categorias)


# ─────────────────────────────────────────
# PRODUTOS — EDITAR
# ─────────────────────────────────────────
@app.route("/produtos/<int:id_produto>/editar", methods=["GET", "POST"])
def editar_produto(id_produto):
    if request.method == "POST":
        try:
            dados = {
                "nome": request.form["nome"],
                "preco": float(request.form["preco"])
            }
            supabase.table("produto").update(dados).eq("id_produto", id_produto).execute()
            limpar_cache_produtos()
            flash("Produto atualizado com sucesso!", "sucesso")
            return redirect(url_for("listar_produtos"))
        except Exception as e:
            flash(f"Erro ao editar produto: {e}", "erro")

    try:
        resp = supabase.table("produto").select("*").eq("id_produto", id_produto).execute()
        produto = resp.data[0] if resp.data else None
        resp_cat = supabase.table("categoria").select("*").execute()
        categorias = resp_cat.data or []
    except Exception as e:
        flash(f"Erro ao carregar produto: {e}", "erro")
        return redirect(url_for("listar_produtos"))

    return render_template("produto_form.html", produto=produto, categorias=categorias)


# ─────────────────────────────────────────
# PRODUTOS — EXCLUIR
# ─────────────────────────────────────────
@app.route("/produtos/<int:id_produto>/excluir", methods=["POST"])
def excluir_produto(id_produto):
    try:
        supabase.table("produto").delete().eq("id_produto", id_produto).execute()
        limpar_cache_produtos()
        flash("Produto excluído com sucesso!", "sucesso")
    except Exception as e:
        flash(f"Erro ao excluir produto: {e}", "erro")
    return redirect(url_for("listar_produtos"))


# ─────────────────────────────────────────
# VIEW — RELATÓRIO DE ESTOQUE
# ─────────────────────────────────────────
@app.route("/relatorio")
def relatorio_estoque():
    try:
        resp = (
            supabase.table("vw_relatorio_estoque")
            .select("*")
            .order("id_produto")
            .execute()
        )
        dados = resp.data or []
        return render_template("relatorio.html", dados=dados)
    except Exception as e:
        flash(f"Erro ao consultar relatório: {e}", "erro")
        return render_template("relatorio.html", dados=[])


# ─────────────────────────────────────────
# FUNCTION — CALCULAR VALOR DO ESTOQUE
# ─────────────────────────────────────────
@app.route("/calcular", methods=["GET", "POST"])
def calcular_valor():
    resultado = None
    produto_info = None

    try:
        resp = supabase.table("produto").select("*").order("id_produto").execute()
        produtos = resp.data or []
    except Exception as e:
        produtos = []
        flash(f"Erro ao carregar produtos: {e}", "erro")

    if request.method == "POST":
        try:
            id_produto = int(request.form["id_produto"])
            resp_prod = (
                supabase.table("produto")
                .select("*")
                .eq("id_produto", id_produto)
                .execute()
            )
            produto_info = resp_prod.data[0] if resp_prod.data else None

            resp = supabase.rpc(
                "calcular_valor_estoque",
                {"p_id_produto": id_produto}
            ).execute()

            resultado = resp.data
        except Exception as e:
            flash(f"Erro ao calcular valor: {e}", "erro")

    return render_template("calcular.html",
                           produtos=produtos,
                           resultado=resultado,
                           produto_info=produto_info)


# ─────────────────────────────────────────
# PROCEDURE — MOVIMENTAÇÕES
# ─────────────────────────────────────────
@app.route("/movimentacao", methods=["GET", "POST"])
def movimentacao():
    mensagem_retorno = None

    try:
        resp = supabase.table("produto").select("*").order("id_produto").execute()
        produtos = resp.data or []
    except Exception as e:
        produtos = []
        flash(f"Erro ao carregar produtos: {e}", "erro")

    if request.method == "POST":
        try:
            id_produto = int(request.form["id_produto"])
            quantidade = int(request.form["quantidade"])
            tipo = request.form["tipo"]  # ENTRADA ou SAIDA

            resp = supabase.rpc(
                "executar_movimentacao_estoque",
                {
                    "p_id_produto": id_produto,
                    "p_quantidade": quantidade,
                    "p_tipo": tipo
                }
            ).execute()

            limpar_cache_produtos()
            mensagem_retorno = resp.data
            flash(f"Movimentação registrada: {mensagem_retorno}", "sucesso")
        except Exception as e:
            flash(f"Erro ao registrar movimentação: {e}", "erro")

    return render_template("movimentacao.html",
                           produtos=produtos,
                           mensagem_retorno=mensagem_retorno)


# ─────────────────────────────────────────
# HISTÓRICO DE MOVIMENTAÇÕES
# ─────────────────────────────────────────
@app.route("/historico")
def historico():
    try:
        resp = (
            supabase.table("movimentacao_estoque")
            .select("*")
            .order("data_movimentacao", desc=True)
            .execute()
        )
        movimentacoes = resp.data or []
        return render_template("historico.html", movimentacoes=movimentacoes)
    except Exception as e:
        flash(f"Erro ao consultar histórico: {e}", "erro")
        return render_template("historico.html", movimentacoes=[])


if __name__ == "__main__":
    app.run(debug=True)
