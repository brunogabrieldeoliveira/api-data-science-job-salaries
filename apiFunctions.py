# importar conexao mydb
import mydbConnection as mydb

# cria o cursor para o mydb
myCursor = mydb.ponteiroMydb()

# funções da API

# cria 
#-----------------------------

# deleta
#-----------------------------

# altera
#-----------------------------

# consulta
#-----------------------------

# retorna todos os jobs
def returnAllJobs():
    
    # consulta view vw_jobs
    myCursor.execute("select * from vw_jobs")
    myResultado= myCursor.fetchall()
    return myResultado
    
"""    
for i in myResultado:
    print(i)

"""