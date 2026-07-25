from flask import render_template, Blueprint,redirect,session,request,url_for


login_bp = Blueprint('login',__name__)

@login_bp.route('/')
def login():
    return render_template('login.html')

    
@login_bp.route('/autenticar', methods=('POST','GET'))
def autenticar():
    
    if request.form['txtsenha'] == 'admin':
        session['usuario_logado'] = request.form['txtlogin']
        return redirect(url_for('painel.escolha'))
    else:
        return render_template('login.html',
                        mensagem = 'Login ou senha incorreto')

    
@login_bp.route('/sair')
def sair():
    session.pop('usuario_logado', None)
    return redirect(url_for('login'))



