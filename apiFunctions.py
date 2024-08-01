# bibliotecas
import apiMysqlConnection as mydb
from flask import jsonify

# cria o cursor para o mydb
myCursor = mydb.ponteiroMydb()

# funções da API

# geral
#-----------------------------

# retorna lista com todos os jobs 
def retornaListaTodosJobs():
    myCursor.execute("select * from vw_jobs")
    jobs= myCursor.fetchall()

    listaJobs= []
    for item in jobs:
        # add item a lista
        listaJobs.append(
            {
                "ID": item[0],
                "Empresa": item[1],
                "Localizacao": item[2],
                "Emprego": item[3]
            }
        )
    return listaJobs


# cria 
#-----------------------------

# deleta
#-----------------------------

# altera
#-----------------------------

# consulta
#-----------------------------

# retorna Json todos jobs
def retornaJsonTodosJobs():
    return jsonify(retornaListaTodosJobs())

# retorna Json pelo nome da empresa
def retornaJsonEmpresa(nomeEmpresa):
    myCursor.execute("select * from vw_jobs where Empresa= " + "'" + nomeEmpresa + "'")
    jobs= myCursor.fetchall()
    
    if len(jobs) == 0:
        return {'ID': 0, 'Empresa': '', 'Localizacao': '', 'Emprego': ''}

    listaJobs= []
    for item in jobs:
        # add item a lista
        listaJobs.append(
            {
                "ID": item[0],
                "Empresa": item[1],
                "Localizacao": item[2],
                "Emprego": item[3]
            }
        )

    return listaJobs

# print(retornaJsonEmpresa("CACI"))

# retorna Json pelo nome do emprego
def retornaJsonEmprego(nomeEmprego):
    myCursor.execute("select * from vw_jobs where Emprego= " + "'" + nomeEmprego + "'")
    jobs= myCursor.fetchall()
    
    if len(jobs) == 0:
        return {'ID': 0, 'Empresa': '', 'Localizacao': '', 'Emprego': ''}

    listaJobs= []
    for item in jobs:
        # add item a lista
        listaJobs.append(
            {
                "ID": item[0],
                "Empresa": item[1],
                "Localizacao": item[2],
                "Emprego": item[3]
            }
        )

    return listaJobs

# chamadas (teste)

# print(retornaJsonTodosJobs())
# print(retornaJsonEmpresa("CACI"))
# print(retornaJsonEmprego("Senior Data Scientist"))