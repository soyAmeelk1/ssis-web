from app import mysql

class Colleges(object):
    def __init__(self, id=None, name=None, code=None):
        self.id = id
        self.name = name
        self.code = code

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO colleges(code, name) \
            VALUES('{self.code}', '{self.name}')"

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def edit(cls,id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM colleges WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def update(cls,id,code,name):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE colleges
            SET code = %s,
                name = %s
            WHERE id = %s
            """, (code, name, id))
        mysql.connection.commit()

    @classmethod
    def refer(cls):
        cursor = mysql.connection.cursor()

        sql = f"SELECT code FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result