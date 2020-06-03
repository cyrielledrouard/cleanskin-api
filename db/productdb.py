from db.genericdb import *


def select_products():
    try:
        cnx = connection_db()
    except Exception as e:
        print("Failed to connect database:" + str(e))
        return None
    sql_select_query = "SELECT * FROM product"
    cursor = cnx.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    disconnection_db(cnx)
    return records


def select_products_by_id(id):
    try:
        cnx = connection_db()
    except Exception as e:
        print("Failed to connect database:" + str(e))
        return None
    sql_select_query = "SELECT * FROM product WHERE id = %d" % id
    cursor = cnx.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchone()
    disconnection_db(cnx)
    return records


def insert_product(id, name, brand, type, price):
    try:
        cnx = connection_db()
    except Exception as e:
        print("Failed to connect database:" + str(e))
        return None
    sql_insert_query = "INSERT INTO product (id, name, brand, type, price) VALUES (%d, '%s', '%s', '%s', %f)" % (id, name, brand, type, price)
    cursor = cnx.cursor()
    cursor.execute(sql_insert_query)
    cnx.commit()
    disconnection_db(cnx)
    return True


def replace_product(name, brand, type, price, id):
    try:
        cnx = connection_db()
    except Exception as e:
        print("Failed to connect database:" + str(e))
        return None
    sql_update_query = "UPDATE product SET name = '%s', brand = '%s', type = '%s', price = %f  WHERE id = %d" % (name, brand, type, price, id)
    cursor = cnx.cursor()
    cursor.execute(sql_update_query)
    cnx.commit()
    disconnection_db(cnx)
    return True


def delete_product_db(id):
    try:
        cnx = connection_db()
    except Exception as e:
        print("Failed to connect database:" + str(e))
        return None
    sql_delete_query = "DELETE FROM product WHERE id = %d" % id
    cursor = cnx.cursor()
    cursor.execute(sql_delete_query)
    cnx.commit()
    disconnection_db(cnx)
    return True
