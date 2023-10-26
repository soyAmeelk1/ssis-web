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

    @classmethod
    def edit(cls,id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM students WHERE id = {id}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
    
    @classmethod
    def update(cls,id,id_number,first_name,last_name,course_id,year,gender):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE students
            SET id_number = %s,
                first_name = %s,
                last_name = %s,
                course_id = %s,
                year = %s,
                gender = %s
            WHERE id = %s
            """, (id_number, first_name, last_name, course_id, year, gender, id))
        mysql.connection.commit()