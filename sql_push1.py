import mysql.connector

filepath = 'C:\Users\Owner\OneDrive\Documents\Python\sql'

with open('host.txt') as g:
  hostname = g.read()

with open('db.txt') as f:
  dbname = f.read()

with open('username.txt') as h:
  username = h.read()

with open('pwd.txt') as i:
  pwd = i.read()

mydb = mysql.connector.connect(
  host=hostname,
  user=username,
  password=pwd,
  database=dbname
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE usernames (name VARCHAR(255), address VARCHAR(255))")