from app import mysql

class Courses(object):
    def __init__(self, id=None, name=None, code=None, college_id=None):
        self.id = id
        self.name = name
        self.code = code
        self.college_id = college_id

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * FROM courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    def add(self):
        cursor = mysql.connection.cursor()

        sql = f"INSERT INTO courses(code, name, college_id) \
            VALUES('{self.code}', '{self.name}', '{self.college_id}')"

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def refer(cls):
        cursor = mysql.connection.cursor()

        sql = f"SELECT code FROM courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
