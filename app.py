from flask import Flask, render_template, request, redirect,session , url_for
from routes.login import login_bp

armazen = {}
#usuario_s = {}
lista = []
#usuario_senha = []

app = Flask(__name__)

app.secret_key = 'Meucodigoshow'


@app.route('/relatorio', methods=['GET',])
def relatorio():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('relatorio.html',
                            listas = lista)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        armazen['categoria'] = request.form['txtcategoria'].strip().lower() 
        if armazen["categoria"].isnumeric():  
            armazen.clear() 
            return render_template('cadastro.html',
                            mensagem= "Digite letras e números")
        
        armazen['produto'] = request.form['txtproduto']
        if armazen["produto"].isnumeric():  
            armazen.clear() 
            return redirect('/cadastro')
        for analise in lista:  
                if analise["produto"] == armazen["produto"]: 
                    armazen.clear()
                    return render_template('cadastro.html',
                                           mensagem = "Esse produto já foi cadastrado!")
                
        armazen['preco'] = float(request.form['numberpreco'])
        armazen['quantidade'] = int(request.form['numberquantidade'])
        lista.append(armazen.copy())
        armazen.clear()
        return redirect('/relatorio')

    return render_template('cadastro.html')


@app.route('/pesquisa_cat',methods=('GET','POST'))
def pesquisa_cat():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        resultado = []  
        categoria = request.form['txtpesquisaa'].strip().lower() 
        for analise in lista: 
            if analise['categoria'] == categoria:
                resultado.append(analise) 
        return render_template(
            'resultado_pesqui_cat.html',
            cat=resultado)
                
    else:   
        return render_template('pesquisa_cat.html')
    

@app.route('/pesquisa_pro', methods=('GET','POST'))
def pesquisa_pro():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        resultado = []  
        pesquisa = False
        categoria = request.form['txtpesquisaa'].strip().lower() 
        for analise in lista: 
            if analise['produto'] == categoria: 
                pesquisa = True 
                print(analise)  
                
        if pesquisa == False: 
            return render_template('pesquisa_pro.html',
                            mensagem = "Produto não encontrado")
            
        for analise in lista: 
            if analise['produto'] == categoria:
                resultado.append(analise) 
        return render_template(
            'resultado_pesqui_pro.html',
            pro=resultado)
                 
    else:   
        return render_template('pesquisa_pro.html')
    
@app.route('/deposito', methods=('GET','POST'))
def deposito():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
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
        return redirect(url_for('login'))
    if request.method == 'POST':
        produto = session['produto']
        for analise in lista:
            if analise['produto'] == produto:
                
                quantidade = int(request.form['numberquantidade'])
                analise['quantidade'] += quantidade
                session.pop('produto', None)
                return redirect(url_for('relatorio'))

    return render_template('depositando.html')


@app.route('/escolha')
def escolha():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    return render_template('escolha.html')
  #=======================================================================================================
  #  
@app.route('/retirada', methods=('POST','GET'))
def retirada():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
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
        return redirect(url_for('login'))
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

if __name__ == '__main__':
    app.run(debug=True)