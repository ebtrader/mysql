import os
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

# https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples

# filepath = 'C:\Users\Owner\OneDrive\Documents\Python\sql'
data_folder = 'C:/Users/Owner/OneDrive/Documents/Python/sql'

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

connection_string = 'mysql+mysqlconnector://' + username + ':' + pwd + '@' + hostname + '/' + dbname
engine = create_engine(connection_string)

# with engine.connect() as connection:
#   connection.execute(text("CREATE TABLE sample (name VARCHAR(50), address VARCHAR(50))"))

df = pd.read_csv('address_book.csv')
print(df)

# conn = engine.connect()
# df.to_sql('address_table', con=engine) # creates table from df

df.to_sql('address_table', con=engine, if_exists='append') # appends table

