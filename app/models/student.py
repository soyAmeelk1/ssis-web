from app import mysql

class Students(object):
    def __init__(
        self,
        id=None,
        firstname=None,
        lastname=None,
        coursecode=None,
        year=None,
        gender=None,
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.coursecode = coursecode
        self.year = year
        self.gender = gender

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result