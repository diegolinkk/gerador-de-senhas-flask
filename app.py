from flask import Flask,request,render_template
from random import choice

app = Flask(__name__)

#gerando função de gerar senha
def gerar_senha(quantidade = 0,tamanho = 0, tipo = 1):
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '1234567890'
    caracteres_especiais = '#@$&*+=-_'

    if tipo == 1:
        caracteres = letras
    elif tipo == 2:
        caracteres = letras + numeros
    else:
        caracteres = letras + numeros + caracteres_especiais

    senhas = []
    for _ in range(quantidade):
        senha = '' #zera senha
        for _ in range(tamanho):
            senha += choice(caracteres)
        
        senhas.append(senha)
    
    return senhas

@app.route('/',methods = ['GET','POST'])
def hello():
    if request.method == 'POST':
        quantidade = int(request.form['quantidade'])
        tamanho = int(request.form['tamanho'])
        tipo = int(request.form['tipo'])
        senhas = gerar_senha(quantidade,tamanho,tipo)
        
        texto = "Senhas Geradas </br> <ol>"
        for senha in senhas:
            texto += '<li>'
            texto += senha
            texto += '</li>'
        
        texto += '</ol>'
        return texto

    return render_template('form.html')