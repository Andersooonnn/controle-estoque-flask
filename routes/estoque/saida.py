from flask import Blueprint, redirect,url_for,request, session, render_template
from routes.dados import lista, armazen

retirada_bp = Blueprint('retirada',__name__)

@retirada_bp.route('/retirada', methods=('POST','GET'))
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
                return redirect(url_for('retirada.retirando'))

        if pesquisa == False: 
            return render_template('retirada.html',
                            mensagem = "Produto não encontrado")
        
    else:
        return render_template('retirada.html')

#Próxima manutenção: Fazer o programa identificar quantidade maxima para poder retirar, assim não ficar com número negativo
#no estoque

@retirada_bp.route('/retirando', methods=('POST','GET'))
def retirando():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    
    if request.method == 'POST':
        produto = session['produto']
        for analise in lista:
            if analise['produto'] == produto:
                quantidade = int(request.form['numberquantidade'])
                if quantidade > analise['quantidade']:
                    return render_template('retirando.html',
                                    info = f'Negado! Quantidade em estoque {analise['quantidade']}')
                else:
                    analise['quantidade'] -= quantidade
                    session.pop('produto', None)
                    return redirect(url_for('relatorio.relatorio'))

    return render_template('retirando.html')