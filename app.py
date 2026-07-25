from flask import Flask, render_template, request, redirect,session , url_for
from routes.login import login_bp
from routes.painel import painel_bp
from routes.buscas import pesquisa_bp
from routes.cadastro import cadastro_bp
from routes.relatorio import relatorio_bp
from routes.estoque.deposito import deposito_bp
from routes.estoque.saida import retirada_bp
from routes.dados import lista , armazen


app = Flask(__name__)

app.secret_key = 'Meucodigoshow'

app.register_blueprint(login_bp)
app.register_blueprint(painel_bp)
app.register_blueprint(pesquisa_bp)
app.register_blueprint(cadastro_bp)
app.register_blueprint(relatorio_bp)
app.register_blueprint(deposito_bp)
app.register_blueprint(retirada_bp)

if __name__ == '__main__':
    app.run(debug=True)