# conexão com o database
import mysql.connector

# obtendo as credencias do db
from credentials import dbConnection

# criando a conexão com o db
mydb= mysql.connector.connect(
    host= dbConnection.get('HOST'),
    user= dbConnection.get('USER'),
    password= dbConnection.get('KEY'),
    database= dbConnection.get('DATABASE')
)

# criando o apontamento para o db
myCursor = mydb.cursor()

# função retorna apontamento db
def ponteiroMydb():
    return myCursor