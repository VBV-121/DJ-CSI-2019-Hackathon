import mysql.connector
for x in range(5):
    name=input("Enter Name : ")
    print(name)
    income=int(input("Enter Income : "))
    texpense=int(input("Enter Total Expense : "))
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="trial")
    mycursor = mydb.cursor()
    idlist = mycursor.execute("SELECT id FROM account")
    idlist = mycursor.fetchall()
    sql = "INSERT INTO account VALUES(%s, %s, %s,%s )"
    val = (len(idlist)+1,name,texpense,income)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Record Inserted.")
