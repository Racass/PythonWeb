import mysql.connector
try:
    from MySQL.database import DataBase
except ImportError:
    from database import DataBase

class mySQL(DataBase):
        
    def execModQuery(self, query: str) -> int:
        myCursor = self.myDB.cursor()
        myCursor.execute(query)
        if(self.autoCommit):
            self.myDB.commit()
        return myCursor.rowcount
    def execReadQuery(self, query: str) -> tuple:
        myCursor = self.myDB.cursor()
        myCursor.execute(query)
        return myCursor.fetchall()
    def commit(self):
        self.myDB.commit()
    def getDBConn(self):
        mydb = mysql.connector.connect(
            host="192.168.1.41",
            user="rafael",
            passwd="rafael36",
            database="PythonTests"
        )
        return mydb