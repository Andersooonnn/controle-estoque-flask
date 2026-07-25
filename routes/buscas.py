from flask import Blueprint , redirect,url_for,request, render_template, session
from routes.dados import lista ,armazen


pesquisa_bp = Blueprint('pesquisa',__name__)

@pesquisa_bp.route('/pesquisa_cat',methods=('GET','POST'))
def pesquisa_cat():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
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
    