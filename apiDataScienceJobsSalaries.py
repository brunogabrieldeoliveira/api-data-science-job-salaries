# importar funções da API
import apiFunctions as af 

# bibliotecas da API
from flask import Flask, jsonify

# inicia a instância do Flask
app= Flask(__name__)

# Construir as funcionalidades

# home
@app.route('/')
def homepage():
    return 'A API está no ar'

# retorna todos os jobs
@app.route('/alljobs')
# retorna todos os jobs
def returnAllJobs():
    jobs= []
    for item in af.returnAllJobs():
        # add item a lista
        jobs.append(
            {
                "ID": item[0],
                "Empresa": item[1],
                "Localizacao": item[2],
                "Emprego": item[3]
            }
        )
    # return jobs
    return jsonify(jobs)


# roda a API
app.run(host='0.0.0.0')