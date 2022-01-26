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
                Date VARCHAR(3),
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


    def insert_subject(self, name, date, time, teacher, link):
        db = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database="subject_system"
                )
        cursor = db.cursor()
        sql = "INSERT INTO subjects(SubjectName, Time, Teacher, Link) VALUES(%s, %s, %s, %s, %s)"
        val = (name , date, time, teacher, link)
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

    def update_subject(self, sub_id, name, date, time, teacher, link):
        db = mysql.connector.connect(
                host=self._host,
                user=self._username,
                password=self._password,
                database="subject_system"
                )
        cursor = db.cursor()
        sql = "UPDATE subjects SET SubjectName=%s, Date=%s, Time=$s, Teacher=%s, Link=%s WHERE Id=%s"
        val = (name, date, time, teacher, link, sub_id)
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
    db.insert_subject('digital and analog', 'Mon', '9:00', 'Danucha Prasertsom', 'https://classroom.google.com/u/1/c/NDUwNzE2MzU5NjM3')
    db.insert_subject('sofware dev', 'Mon', '13:00', 'Damrongrit Setsirichok', 'https://zoom.us/j/7505560466?pwd=SzZFblRleVVsaVE2L0YweGgwNDBVUT09')
    db.insert_subject('physology for entorprenuor', 'Tue', '9:00', 'Prajuc Patitus', 'https://classroom.google.com/u/1/c/NDUwNzkzODcwNDIz')
    db.insert_subject('general math', 'Tue', '13:00', 'Kanokwan Sitti...', 'https://zoom.us/rec/share/dKY4Nucemu4dm-8Ymj5djQBXaIjvcNjocP-ogtTcvGdNnwK7Ml0RpZCg4ai9m1CG.m7gvS0tO9CnbQYtp')
    db.insert_subject('computer organization', 'Wen', '9:00', 'Danucha Prasertsom', 'https://classroom.google.com/u/1/c/NDUwNzE1NTY4OTU1')
    db.insert_subject('Ubicom', 'Wen', '13:00', 'Yuenyong Nilsiam', ' https://zoom.us/j/6341417809?pwd=bnRLVXlMTnh0c3JaZjJSSmVQNTZvdz09')
    db.insert_subject('Network engineer', 'Thu', '9:00', 'Natthinan Sakulpakdee', 'https://classroom.google.com/u/1/c/NDUxMjA3NTkxMjYy')
    db.insert_subject('sofware dev', 'The', '13:00', 'Damrongrit Setsirichok', 'https://zoom.us/j/7505560466?pwd=SzZFblRleVVsaVE2L0YweGgwNDBVUT09')
    db.select_all()
    while True:
        pass
