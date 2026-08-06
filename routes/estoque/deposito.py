from flask import Blueprint, session , redirect , request , render_template , url_for
from routes.dados import lista, armazen


deposito_bp = Blueprint("deposito",__name__)

@deposito_bp.route('/deposito', methods=('GET','POST'))
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
                return redirect(url_for('deposito.depositando'))

        if pesquisa == False: 
            return render_template('deposito.html',
                            mensagem = "Produto não encontrado")
        
    else:
        return render_template('deposito.html')


@deposito_bp.route('/depositando', methods=('POST','GET'))
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
                return redirect(url_for('deposito.deposito'))
    produtos = session['produto']        
    for analisando in lista:
        if analisando['produto'] == produtos:
            return render_template('depositando.html',
                                msn = f'Produto: {analisando['produto']} | Quantidade: {analisando['quantidade']}')
