#conectando ao banco
import sqlite3
from sqlite3 import Error



#### CRIANDO CONEXÃO COM O BANCO ####
db = 'db.db'
conn = sqlite3.connect(db)



#### CRIANDO TABELA NO BANCO ####
sql = """CREATE TABLE IF NOT EXISTS tb_usuarios(ID INTEGER PRIMARY KEY AUTOINCREMENT, usuario VARCHAR(80), senha VARCHAR(20))"""

with conn:
        cur = conn.cursor()
        cur.execute(sql)


con = sqlite3.connect(db)


def create_inf(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO tb_usuarios (usuario, senha) VALUES(?, ?)"
        cur.execute(query, i)



