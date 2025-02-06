import mysql.connector
from mysql.connector import errorcode

class DBAccess:
   
    username = "root"
    password = "kalib"
    host = " 10.105.12.226"
    database = "nea"
    connection = ""
    cursor = ""
   
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(user=self.username,password=self.password,
            host=self.host,
            database=self.database)
            self.cursor = self.connection.cursor(prepared=True)                    
           
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
       # else:
            #connection.close()
               
    def insert(self, sqlStatement, valuesList):
        self.cursor.execute(sqlStatement, valuesList) # sending a prepared statement with a list of values in order
        self.connection.commit() # confirm it is the correct operation
       
    def close(self):
        self.connection.close()