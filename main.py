from flask import Flask, render_template, request, redirect

armazen = {}
lista = []

app = Flask(__name__)

@app.route('/relatorio')
def relatorio():
    return render_template('relatorio.html',
                           listas = lista)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

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
                    print("Esse produto ja foi cadastrados")
                    return render_template('cadastro.html',
                                           mensagem = "Esse produto já foi cadastrado!")
                
        armazen['preco'] = request.form['numberpreco']
        armazen['quantidade'] = request.form['numberquantidade']
        lista.append(armazen.copy())
        armazen.clear()
        return redirect('/relatorio')

    return render_template('cadastro.html')


@app.route('/pesquisa_cat',methods=('GET','POST'))
def pesquisa_cat():
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
    
             
@app.route('/escolha')
def escolha():
    return render_template('escolha.html')

if __name__ == '__main__':
    app.run(debug=True)