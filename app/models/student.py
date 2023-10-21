from app import mysql

class Students(object):
    def __init__(
        self,
        id=None,
        id_number=None,
        first_name=None,
        last_name=None,
        course_id=None,
        year=None,
        gender=None,
    ):
        self.id = id
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.year = year
        self.gender = gender

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO students(id_number, first_name, last_name, course_id, year, gender) \
            VALUES('{self.id_number}', '{self.first_name}', '{self.last_name}', '{self.course_id}', '{self.year}', '{self.gender}')"
        
        cursor.execute(sql)
        mysql.connection.commit()