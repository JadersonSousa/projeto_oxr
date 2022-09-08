import sqlite3
from sqlite3 import Error

db = 'logs.db'

try:
    connect = sqlite3.connect(db)
    
    if connect:
        print("Sucesso: Exito na conexão do banco local SQLITE")
except Error as error:
    
    print("Erro: Erro na conexão do banco SQLITE", error)

def insertLog(i):
    try:
        with connect:
            cursor = connect.cursor()
            sql = "INSERT INTO tb_user_logs(id, nome, user_login, data_login) VALUES(?,?,?,?)"
            cursor.execute(sql, i)
            print("Usuário inserido no db LOCAL: ", cursor)

    except Error as ErrorInsertUser:
        print("Usuário ja existe no db LOCAL: ", ErrorInsertUser)



def inforUserLog():
    try:
        with connect:
            cursor = connect.cursor()
            sql = "SELECT * FROM tb_user_logs"
            cursor.execute(sql)
            userLog = cursor.fetchone()
            return userLog
            #print("Sucesso: Usuário encontrado no db LOCAL: ",userLog)

    except Error as ErrorShowtUser:
        print("Erro: Usuário não encontrado no db LOCAL: ", ErrorShowtUser)