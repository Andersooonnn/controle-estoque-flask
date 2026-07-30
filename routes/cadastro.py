from flask import Blueprint, redirect, url_for, render_template, request , session
from routes.dados import lista,armazen

cadastro_bp = Blueprint('cadastro',__name__)

# informar que o produto foi cadastrado com sucesso e dar continuidade ao cadastro

@cadastro_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))

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