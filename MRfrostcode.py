import mysql.connector
from mysql.connector import errorcode

class DBAccess:
   
    __username = "root"
    __password = "kalib"
    __host = " 10.105.12.226"
    __database = "nea"
    connection = ""
    cursor = ""
   
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(user=self.__username,password=self.__password,
            host=self.__host,
            database=self.__database)
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
    def saveTwoDlistToCSVFile(filename, externList):
        myFile = open(fileName, "w")
        for keyword in externList:
            counter = 0
            lineToWrite=""
            while counter < len(keyword)-1:
                lineToWrite = lineToWrite+keyword[counter]+ ","
                counter = counter+1
            lineToWrite = lineToWrite + keyword[len(keyword)-1] + "\n"
            myFile.write(lineToWrite)
        myFile.close()
    def print2DListWithoutTheCrap(listToPrint):
        column = 0
        while column < len(keywords):
            row=0
            lineToPrint = ""
            while row < len(keywords[column]):
                lineToPrint = lineToPrint + keywords[column][row] + " "
                row = row + 1
            column = column + 1
            print(lineToPrint)


    def openFileInto2DList(fileName):
        myFile = open("myText.txt" , "r")
        keywords= []
        for line in myFile:
            line = line.strip("\n")
            keywordsAndDefinition = line.split(",")
            keywords.append(keywordsAndDefinition)
        myFile.close()
        return keywords
        keywords = openFileInto2DList("myText")
        print2DListWithoutTheCrap(keywords)