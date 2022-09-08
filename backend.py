import mysql.connector
from main import *

global resultUser

connect = mysql.connector.connect(
    host='containers-us-west-16.railway.app',
    port=5569,
    user='root',
    password='4CJjy8kG2MJ0VdMJoq5x',
    database='railway'
)

if connect.is_connected():
    db_info = connect.get_server_info()
    print("database connect success")

def doLogin(user, password):
    sqlUsers = "SELECT * FROM tb_users WHERE login_user='{}' and password='{}'".format(user, password)
    cursor = connect.cursor()
    cursor.execute(sqlUsers)
    users = cursor.fetchone()
    return users
    
        