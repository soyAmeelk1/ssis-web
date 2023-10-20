from app import mysql

class Colleges(object):
    def __init__(self, id=None, name=None, code=None):
        self.id = id
        self.name = name
        self.code = code

    # def add(self): #image_url
    #     cursor = mysql.connection.cursor()

    #     sql = f"INSERT INTO students(id_number, first_name, last_name, course, year, gender) \
    #         VALUES('{self.id_number}', '{self.first_name}', '{self.last_name}', '{self.course}', '{self.year}', '{self.gender}')" #image_url

    #     cursor.execute(sql)
    #     mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * FROM colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result