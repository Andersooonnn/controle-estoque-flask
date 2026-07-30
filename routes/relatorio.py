from flask import Blueprint, session,redirect,render_template , url_for
from routes.dados import lista, armazen

relatorio_bp = Blueprint('relatorio',__name__)



@relatorio_bp.route('/relatorio', methods=['GET',])
def relatorio():
    if 'usuario_logado' not in session:
        return redirect(url_for('login.login'))
    else:
        return render_template('relatorio.html',
                            listas = lista)