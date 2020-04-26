import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="counter_app",
  passwd="mypassword",
  database="counter",
)
my_cursor=mydb.cursor()

sqlstuff="INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s,%s,%s,%s,%s,%s)"
record1=(3, 'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway')

my_cursor.execute(sqlstuff, record1)
mydb.commit()
