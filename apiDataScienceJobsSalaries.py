# bibliotecas
import apiFunctions as af 
from flask import Flask

# inicia a instância do Flask
app= Flask(__name__)

# Construir as funcionalidades

# home
@app.route('/')
def homepage():
    return 'A API está no ar'

# retorna todos os jobs
@app.route('/alljobs')
def retornaJsonTodosJobs():
    return af.retornaJsonTodosJobs()
    
# roda a API
app.run(host='0.0.0.0')