import mysql.connector
from mysql.connector import errorcode
#"192.168.3.55"#"10.105.13.228"# "127.0.0.1"#"10.105.14.45"
class DBAccess:
    username = "root"
    password = "kalib"
    host ="127.0.0.1"
    database = "nea2"
    connection = ""
    cursor = ""
   
    def __init__(self):  
        
        try:  
            self.connection = mysql.connector.connect(user=self.username,password=self.password,  
            host=self.host,  
            database=self.database)  
            self.DBcursor = self.connection.cursor(prepared=True)  
                                
        except mysql.connector.Error as err:  
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:  
                print("Something is wrong with your user name or password")  
            elif err.errno == errorcode.ER_BAD_DB_ERROR:  
                print("Database does not exist")  

            else:  
                print(err)  
    
    def insert(self, sqlStatement, valuesList):  
        self.DBcursor.execute(sqlStatement, valuesList)  
        self.connection.commit() 
    
    def close(self):  
        self.connection.close()  
    
    def select(self, sqlStatement, valuesList=[]):  
        mycursor =self.connection.cursor()  
        mycursor.execute(sqlStatement, valuesList)  
        data = mycursor.fetchall()
        self.connection.commit() 

   

    