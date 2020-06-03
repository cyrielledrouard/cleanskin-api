import mysql.connector


def connection_db():
    cnx = mysql.connector.connect(host='127.0.0.1', database='beauty_products', user='root')
    return cnx


def disconnection_db(cnx):
    cnx.close()



