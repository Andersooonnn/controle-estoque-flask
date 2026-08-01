from flask import Blueprint , redirect,url_for,request, render_template, session
from routes.dados import lista ,armazen

pesquisa_bp = Blueprint('pesquisa',__name__)

# =====================================Area de pesquisa por categoria =====================================

@pesquisa_bp.route('/pesquisa_cat',methods=('GET','POST'))
def pesquisa_cat():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    
    if request.method == 'POST':
        resultado = []  
        pesquisa = False
        categoria = request.form['txtpesquisaa'].strip().lower() 
        for analise in lista: 
            if analise['categoria'] == categoria:
                pesquisa = True
        if pesquisa == False:
            return render_template('pesquisa_cat.html',
                                   msn = 'Produto não encotrado')
        
        for analise in lista: 
            if analise['categoria'] == categoria:
                    resultado.append(analise) 
        return render_template(
            'resultado_pesqui_cat.html',
            cat=resultado)                
    else:   
        return render_template('pesquisa_cat.html')

# =====================================Area de pesquisa por produto =====================================

@pesquisa_bp.route('/pesquisa_pro', methods=('GET','POST'))
def pesquisa_pro():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    
    if request.method == 'POST':
        resultado = []  
        pesquisa = False
        categoria = request.form['txtpesquisaa'].strip().lower() 
        for analise in lista: 
            if analise['produto'] == categoria: 
                pesquisa = True   
                
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
    