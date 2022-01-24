import mysql.connector
from mysql.connector import errorcode
class Database:
    def __init__(self):
        self._host = "mysqldb"
        self._username = "root"
        self._password = "1234"

    def create_database(self):
        try:
            db = mysql.connector.connect(
                    host=self._host,
                    user=self._username,
                    password=self._password
                    )
            cursor = db.cursor()
            cursor.execute("CREATE DATABASE subject_system")
            cursor.close()
            db.close()
            print("Create database completed!")
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))


    def create_table(self):
        try:
            db = mysql.connector.connect(
                    host=self._host,
                    user=self._username,
                    password=self._password,
                    database="subject_system"
                    )
            cursor = db.cursor()
            cursor.execute("""
                CREATE TABLE subjects (
                Id int AUTO_INCREMENT primary key NOT NULL ,
                SubjectName VARCHAR(100), 
                Time time(0),
                Teacher VARCHAR(255),
                Link VARCHAR(255))
            """)
            cursor.close()
            db.close()
            print("Create table completed!")
        except mysql.connector.Error as err:
            if err.errno== errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg) 


    def insert_subject(self, name, time, teacher, link):
        db = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database="subject_system"
                )
        cursor = db.cursor()
        sql = "INSERT INTO subjects(SubjectName, Time, Teacher, Link) VALUES(%s, %s, %s, %s)"
        val = (name , time, teacher, link)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()

    def select_all(self):
        db = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database="subject_system"
                )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM subjects")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result

    def delete_subject(self, sub_id):
        db = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database="subject_system"
                )
        cursor = db.cursor()
        cursor.execute("DELETE FROM subject_system WHERE Id=%s", (sub_id))
        db.commit()
        cursor.close()
        db.close()
        return result

    def update_subject(self, sub_id, name, time, teacher, link):
        db = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database="subject_system"
                )
        cursor = db.cursor()
        sql = "UPDATE subjects SET SubjectName=%s, Time=$s, Teacher=%s, Link=%s WHERE Id=%s"
        val = (name, time, teacher, link, sub_id)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        return result

    def check_connection(self):
        db = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password
                )
        if (db.is_connected()):
            print("Connected")
        else:
            print("Not connected")
        db.close()

if __name__ == "__main__":
    db = Database()
    db.check_connection()
    db.create_database()
    db.create_table()
    while True:
        pass
