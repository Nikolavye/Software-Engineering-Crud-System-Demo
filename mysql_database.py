import pymysql


def get_connection():
    connect = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='items_db',
        charset='utf8'
    )
    return connect


def query(sql):
    connection = get_connection()
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result
    finally:
        connection.close()


def insert_update(sql):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    finally:
        connection.close()


def delete(sql):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
    finally:
        connection.close()


if __name__ == '__main__':
    sql = 'insert into items(name, quantity ,price) values("tree", 19, 82)'
    insert_update(sql)
    sql = 'delete from items where id = 1'
    delete(sql)
    sql = 'SELECT * FROM items'
    res = query(sql)
    print(res)
