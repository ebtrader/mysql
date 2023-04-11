import mysql.connector
import os

# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

# filepath = 'C:\Users\Owner\OneDrive\Documents\Python\sql'
data_folder = 'C:/Users/Owner/OneDrive/Documents/Python/sql'
# data_folder = os.path.abspath(filepath)

hostname_file = os.path.join (data_folder, 'host.txt')
with open(hostname_file) as g:
  hostname = g.read()

db_file = os.path.join (data_folder, 'db.txt')
with open(db_file) as f:
  dbname = f.read()

username_file = os.path.join (data_folder, 'username.txt')
with open(username_file) as h:
  username = h.read()

pwd_file = os.path.join (data_folder, 'pwd.txt')
with open(pwd_file) as i:
  pwd = i.read()

mydb = mysql.connector.connect(
  host=hostname,
  user=username,
  password=pwd,
  database=dbname
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE animals (name VARCHAR(255), address VARCHAR(255))")