import mysql.connector
import urllib.request
from bs4 import BeautifulSoup

#accesing web-scrapping python code
from web_scrapping import calculate_1

#connecting to the mysql database
mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="trial")
mycursor = mydb.cursor()
idlist = mycursor.execute("SELECT * FROM account")
idlist = mycursor.fetchall()

#iteration for performing the bugeting list and investement options
for x in idlist:
    name = x[1]
    texpense = x[2]
    income = x[3]

    saving=0.2*float(income)
    balance=float(income)-saving
    balance -= float(texpense)
    saving += balance
    saving_percent=(saving/float(income))*100

    print("For User : ",name)
    print("your total saving of month is ",saving)
    print("Saving Percentage Is : ",saving_percent)

    if saving_percent>30:
        print("these are the following investement option for you ")
        calculate_1()

    elif saving_percent<=10:
        print("After applying 50-30-20 Rule...")
        texpense=0.8*float(income)
        saving=0.2*float(income)
        print("New Expense is : ",texpense)
        print("New Saving is : ",saving)
