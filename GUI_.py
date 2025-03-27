import customtkinter
from customtkinter import filedialog
import tkinter as tk
import customtkinter as ctk
from smtplib import SMTP
import smtplib
import email
from email.mime.text import MIMEText
import smtplib,email,email.encoders,email.mime.text,email.mime.base
from email.mime.multipart import MIMEMultipart
import sys
import os
from arial_distance.arial_distance import get_distance
import customer
from customer import *
from DBreal import DBAccess
import pandas as pd
import csv
#from PIL import Image - download PyPi somehow



#customtkinter.set_appearance_mode("System")
customtkinter.set_appearance_mode("dark")
#customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

class main(customtkinter.CTk):
    def __init__(self):
        self.dbHandler = DBAccess()
        super().__init__()
        self.geometry("2000x500")
        self.title("Business Profitability Calculator")
        
        self.frame = customtkinter.CTkFrame(self, corner_radius = 10, fg_color = "transparent")
        self.frame.place(relx = 0.35, rely = 0.35, anchor=customtkinter.E)
        
        self.frame2 = customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent")
        self.frame2.place(relx = 0.35, rely = 0.5, anchor=customtkinter.E)
        
        self.entry = customtkinter.CTkEntry(self.frame, placeholder_text="Email Address")
        self.entry.grid( row = 8, column = 10)
        
        
        self.entry2 = customtkinter.CTkEntry(self.frame2, placeholder_text="Import File")
        self.entry2.grid( row = 8, column = 10)
        
        self.frame3 = customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent")
        self.frame3.place(relx = 0.125, rely = 0.15, anchor=customtkinter.NE)
        
        self.textbox = customtkinter.CTkTextbox(self.frame3, width=175, height = 500,font = ("arial",24))
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "\n\n\nWelcome to\nthe Netmatters Business\nProfitability\nCalculator –\nPlease enter\nthe Email\nAddress \nyou wish for\nthe report\nto be sent to!")
        
        self.frame4 = customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent")
        self.frame4.place(relx = 0.325, rely = 0, anchor=customtkinter.NE)
        
        self.textbox1 = customtkinter.CTkTextbox(self.frame4, width=500, height = 50,font = ("arial",28))
        self.textbox1.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox1.insert("0.0", "Business Profitability Calculator")
        
        self.frame5 = customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent",border_color = "gray10")
        self.frame5.place(relx = 0.3625, rely = 0.42, anchor=customtkinter.E)        
        
        self.frame6=customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent")
        self.frame6.place(relx =0.875,rely=0.9,anchor=customtkinter.NW)
        
        self.textbox2 = customtkinter.CTkTextbox(self.frame6, width = 150, height = 25)
        self.textbox2.grid(row = 0, column = 0,padx = (20,20), pady = (20,20),sticky = "nsew")
        self.textbox2.insert("0.0","Created by K.Gulliver")
        
        self.frame7=customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent")
        self.frame7.place(relx =0.4,rely=0.9,anchor=customtkinter.SW)
        
        self.frame8=customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent" )
        self.frame8.place(relx =0.6,rely=0.85,anchor=customtkinter.SW)
        
        self.textbox3 = customtkinter.CTkTextbox(self.frame8, width = 300, height = 500,font = ("arial",24))
        self.textbox3.grid(row = 0, column = 0,padx = (20,20), pady = (20,20),sticky = "nsew",)
        self.textbox3.insert("0.0","\n\n\nThis Business profitability Calculator will analyze the data inputted field by field and decide the most\nprofitable business type to target by SIC code, and\ncreate a detailed report\nexplaining the ratings per business type and email\nthe results to you.")
        
        
        
        self.frame9=customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent",bg_color = "transparent")
        self.frame9.place(relx =0.35,rely=0.5,anchor=customtkinter.E)
        
        
        self.button2 = customtkinter.CTkButton(master=self.frame5, fg_color="gray10",text ="Enter", border_width=2,bg_color = "transparent", text_color=("gray10", "#DCE4EE"),command = self.button_event)
        self.button2.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        
        self.button3 = customtkinter.CTkButton(self.frame9, text='Open File', command=self.UploadAction)
        self.button3.grid()
        
        
        self.frame10=customtkinter.CTkFrame(self, corner_radius = 10,fg_color = "transparent",bg_color = "transparent")
        self.frame10.place(relx =0.5,rely=0.5,anchor=customtkinter.S)
        
    def UploadAction(self,event=open):
        filename = filedialog.askopenfilename()
        print('Selected:', filename)
        self.openFile(filename)
    
    def openFile(self, event): 
        myFile = open(event, "r")
        array = []
        for line in myFile:
            line = line.strip(",")
            line = line.strip("")
            array.append(line) 
        self.saveInDB(array)
        '''
        while True: 
            try: 
                #with open(fileToOpen, "r") as openFile:
                z = open(fileToOpen, "r")
                #openFile.readlines()
                     
                array = [] 
                print(z)
                
                for line in z: 
                    line = line.strip("\n") 
                    #lineSplit = line.split(" ") 
                    array.append(line)
                    print(array) 
                z.close() 
                self.saveInDB(array)
                
            
            except IOError as e: 
                #print("Could not find file :" + fileToOpen + " . Perhaps you forgot your file extension") 
                pass  
                
        '''
        print()
    #def testOpenFile
                # if counter != 0:
            #     counter += 1
            #     for row in dataToSave:
            #         valList = []
                    
            #         valList.append(row)
            #         print(valList)
            #         for val in valList:
    '''        #             print(val)
    def saveInDB(self,dataToSave):
        for i in range(dataToSave):
            if i == 0:
                i=i+1
            elif i != 0:
                    self.dbHandler.insert('INSERT into data2 (customer_ID,postcode,lat,long_,total_sales,turnover_override,staff_count,profit,turnover,estimated_turnover,sic_code) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
            else:
                self.dbHandler.insert('INSERT into data2 (customer_ID,postcode,lat,long_,total_sales,turnover_override,staff_count,profit,turnover,estimated_turnover,sic_code) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
'''
            
    def saveInDB(self,dataToSave):
        for i in dataToSave:
            reader = csv.reader(dataToSave, delimiter=",")
            for column in reader:
                    if column == 10:
                        column = column + str("\n")
                    else:
                        self.dbHandler.insert('INSERT into data2 (customer_ID,postcode,lat,long_,total_sales,turnover_override,staff_count,profit,turnover,estimated_turnover,sic_code) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', column)

    '''def saveInDB(self,dataToSave): 
        for i, row in enumerate(dataToSave):
            if i != 0:
                print(row)
                row = row.split(",")
                #for item in row:
                for i, column in enumerate(dataToSave):
                    if column == 10:
                        column = column + str("\n")
                    #if type(item) != str:
                        #item == str(item)
                else:
                    self.dbHandler.insert('INSERT into data2 (customer_ID,postcode,lat,long_,total_sales,turnover_override,staff_count,profit,turnover,estimated_turnover,sic_code) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
                    print("hi")
'''

    '''def saveInDB(self,dataToSave):
        for i in row(dataToSave):
            if i != 0:
                print(row)
                row = row.split(",")   
                self.dbHandler.insert('INSERT into data2 (customer_ID,postcode,lat,long_,total_sales,turnover_override,staff_count,profit,turnover,estimated_turnover,sic_code) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
     #self.analysis(valList)
    def analysis(self,dataToSave):
        dbHandler = DBAccess()
        for i, row in enumerate(dataToSave):
            
            dbHandler.DBcursor.execute('SELECT customer_ID from data2 where ROW =(%s)',(i,))
            results = self.cursor.fetchone()
            dbHandler.DBcursor.execute('INSERT INTO customer(customer_ID)VALUES(results)')
            
            dbHandler.DBcursor.execute('SELECT postcode from data2 where ROW =(%s)',(i,))
            results2 = self.cursor.fetchone()
            if results2 != "":
                dbHandler.DBcursor.execute('INSERT INTO customer(postcode)VALUES(%s)',(results2,))
            #
            dbHandler.DBcursor.execute('SELECT lat from data2 where ROW = (%s)',(i,))
            results3 = self.cursor.fetchone()
            dbHandler.DBcursor.execute('SELECT long_ from data2 where ROW =(%s)',(i,))
            results4 = self.cursor.fetchone()
            a = results3
            b = results4 
            dbHandler.DBcursor.execute('INSERT INTO customer(distanceRating)VALUES(self.DistanceCalc(%s, %s))',(a,b,))
            #

            #
            dbHandler.DBcursor.execute('SELECT total_sales from data2 where ROW =(%s)',(i,))
            results5 = self.cursor.fetchone()
            x = self.SalesCalc(results5)
            dbHandler.DBcursor.execute('INSERT INTO customer(total_salesRating)VALUES(%s),'(x,))
            #
            if turnover != "":
                 #
                dbHandler.DBcursor.execute('SELECT turnover from data2 where ROW = (%s)',(i,))
                results8 = self.cursor.fetchone()
                z = self.TurnoverCalc(results8)
                dbHandler.DBcursor.execute('INSERT INTO CUSTOMER(turnoverRating) from data2 where ROW= (%s)',(z,))
                #
            elif turnover_override != "":
                #
                dbHandler.DBcursor.execute('SELECT turnover_override from data2 where ROW= (%s)',(i,))
                results6 = self.cursor.fetchone()
                f = self.TurnoverCalc(results6)
                dbHandler.DBcursor.execute('INSERT INTO CUSTOMER(turnover_overrideRating) from data2 where ROW= (%s)',(c,))
                #
            else:
                 #
                dbHandler.DBcursor.execute('SELECT estimated_turnover from data2 where ROW =(%s)',(i,))
                results9 = self.cursor.fetchone()
                c = self.TurnoverCalc(results9)
                dbHandler.DBcursor.execute('INSERT INTO CUSTOMER(turnoverRating) from data2 where ROW= (%s)',(c,))
                #
            #self.TurnoverCalc(results6)
            dbHandler.DBcursor.execute('SELECT staff_count from data2 where ROW =(%s)',(i,))
            results7 = self.cursor.fetchone()
            y = self.StaffCountCalc(results7)
            dbHandler.DBcursor.execute('INSERT INTO CUSTOMER(staff_countRating) from data2 where ROW= (%s)',(x,))
            #self.StaffCountCalc(results7)

           

           
            
            #
            dbHandler.DBcursor.execute('SELECT sic_code from data2 where ROW =(%s)',(i,))
            results10 = self.cursor.fetchone()
            #self.SICcodes(results10)
            #possible implementation in v2
            #

            dbHandler.DBcursor.execute('SELECT profit from data2 where ROW =(%s)',(i,))
            results11 = self.cursor.fetchone()
            d = ProfitCalc(results11)
            dbHandler.DBcursor.execute('INSERT INTO CUSTOMER(profitRating) from data2 where ROW= (%s)',(d,))

        
    def averageCalc(self,dataToSave):
        dbHandler = DBAccess()
        for i, row in enumerate(dataToSave):
            dbHandler.dbCursor.execute('SELECT * from Customer where ROW =(%s)',(i,))'''
                                                                                        
    
    


    def button_event(self):
        self.entry.get()
        self.emailSend()

    def getButton(self):
        print(self.entry.get())

    def commandForButton(self):
        self.email.send()

    def report(self): 
        report1 = "Target Market Group Report: \n Netmatters, the company group you should be targeting the most is ___, as they have a score of 12, and will be best suited for your business-The next company groups you should target are, ___, ___, ___\nas they have scores 11,10 and 9 respectively.\n-The companies with moderately good profitability are, ___, ___, ___\nas they have scores 8,7 and 6 respectively.\n-The final company group to target are __, they have a score of 5.\n-Company groups to avoid are those below a score of 5, such as ___,___,___ and ___.\n"
        return(report1)
    
    def emailSend(self):
        x = str(self.entry.get())
        mainMessage = MIMEMultipart()
        mainMessage['From'] = 'profitabilitycalculator.report@gmail.com'
        mainMessage['To'] = (x)
        mainMessage['Subject'] = 'Report'
        text = self.report()
        
        mainMessage.attach(MIMEText(text))
        try:
            gmailServer = smtplib.SMTP('smtp.gmail.com',587)
            gmailServer.starttls()
            gmailServer.ehlo()
            gmailServer.login('profitabilitycalculator.report@gmail.com', 'eiuw zdoa omif vtfp')
            gmailServer.sendmail('profitabilitycalculator.report@gmail.com',str(x),mainMessage.as_string())
            
            if gmailServer.sendmail == True:
                print("Success!")
            elif gmailServer.sendmail == False:
                print("Error!")
        except Exception as e:
            print(f"Error: {e}")
    def loopForAnalysis(self):
        for x in xList:
            x =x

   
    #def image1(self,imageWithFileExtension):
        #my_image = customtkinter.CTkImage(my_image=image.open(imageWithFileExtension))
        #image_label = customtkinter.CTkLabel(app, image=my_image, text="")  
    
if __name__ == "__main__":
    window = main()

    window.button_event
    
    window.mainloop()
