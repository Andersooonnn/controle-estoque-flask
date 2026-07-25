from flask import Flask, render_template, request, redirect,session , url_for
from routes.login import login_bp
from routes.painel import painel_bp
from routes.buscas import pesquisa_bp
from routes.cadastro import cadastro_bp
from routes.dados import lista , armazen


app = Flask(__name__)

app.secret_key = 'Meucodigoshow'


@app.route('/relatorio', methods=['GET',])
def relatorio():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    else:
        return render_template('relatorio.html',
                            listas = lista)







    
@app.route('/deposito', methods=('GET','POST'))
def deposito():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST': 
        pesquisa = False
        produto = request.form['txtpesquisaa'].strip().lower()
        for analise in lista: 
            if analise['produto'] == produto: 
                session['produto'] = produto
                pesquisa = True 
                return redirect(url_for('depositando'))

        if pesquisa == False: 
            return render_template('deposito.html',
                            mensagem = "Produto não encontrado")
        
    else:
        return render_template('deposito.html')

#fazendo atualização =============================================================================
@app.route('/depositando', methods=('POST','GET'))
def depositando():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        produto = session['produto']
        for analise in lista:
            if analise['produto'] == produto:
                
                quantidade = int(request.form['numberquantidade'])
                analise['quantidade'] += quantidade
                session.pop('produto', None)
                return redirect(url_for('relatorio'))

    return render_template('depositando.html')



  #=======================================================================================================
  #  
@app.route('/retirada', methods=('POST','GET'))
def retirada():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST': 
        pesquisa = False
        produto = request.form['txtpesquisaa'].strip().lower()
        for analise in lista: 
            if analise['produto'] == produto: 
                session['produto'] = produto
                pesquisa = True 
                return redirect(url_for('retirando'))

        if pesquisa == False: 
            return render_template('retirada.html',
                            mensagem = "Produto não encontrado")
        
    else:
        return render_template('retirada.html')

@app.route('/retirando', methods=('POST','GET'))
def retirando():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    if request.method == 'POST':
        produto = session['produto']
        for analise in lista:
            if analise['produto'] == produto:
                
                quantidade = int(request.form['numberquantidade'])
                analise['quantidade'] -= quantidade
                session.pop('produto', None)
                return redirect(url_for('relatorio'))

    return render_template('retirando.html')



app.register_blueprint(login_bp)
app.register_blueprint(painel_bp)
app.register_blueprint(pesquisa_bp)
app.register_blueprint(cadastro_bp)

if __name__ == '__main__':
    app.run(debug=True)