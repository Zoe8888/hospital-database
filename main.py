import mysql.connector

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1', database='HOSPITAL',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
xy = mycursor.execute('Select * from Dentist')
for i in mycursor:
    print(i)

# Insert a record
sql = 'INSERT INTO Dentist VALUES (%s, %s, %s, %s, %s)'
val = ('GDP', 'Godwin', 'Dr Dzvapatsva', '0735887757', '1023450')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, 'record inserted')
mycursor.execute('Select * from Dentist')
for i in mycursor:
    print(i)

# Update a record
update = "UPDATE Dentist SET Dentist_Surname='Myberg' WHERE Dentist_Names='Godwin'"
mycursor.execute(update)
mydb.commit()

print(mycursor.rowcount, 'record inserted')
mycursor.execute('Select * from Dentist')
for i in mycursor:
    print(i)