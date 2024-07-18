# conexão com o database
import mysql.connector

# criando a conexão com o db
mydb= mysql.connector.connect(
    host= 'localhost',
    user= 'user',
    password= '123456',
    database= 'jobs'
)

# criando o apontamento para o db
myCursor = mydb.cursor()

# função retorna apontamento db
def ponteiroMydb():
    return myCursor