from flask import Blueprint , render_template, redirect,url_for,session
from routes.login import login_bp

painel_bp = Blueprint('painel',__name__)

@painel_bp.route('/escolha')
def escolha():
    if 'usuario_logado' not in session:
        return redirect(url_for('login'))
    return render_template('escolha.html')