import os
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

# https://planetscale.com/blog/using-mysql-with-sql-alchemy-hands-on-examples

hostname_file = 'host.txt'
with open(hostname_file) as g:
  hostname = g.read()

# db_file = os.path.join (data_folder, 'db.txt')
db_file = 'db.txt'
with open(db_file) as f:
  dbname = f.read()

# username_file = os.path.join (data_folder, 'username.txt')
username_file = 'username.txt'
with open(username_file) as h:
  username = h.read()

# pwd_file = os.path.join (data_folder, 'pwd.txt')
pwd_file = 'pwd.txt'
with open(pwd_file) as i:
  pwd = i.read()

connection_string = 'mysql+mysqlconnector://' + username + ':' + pwd + '@' + hostname + '/' + dbname
engine = create_engine(connection_string)

# with engine.connect() as connection:
#   connection.execute(text("CREATE TABLE sample (name VARCHAR(50), address VARCHAR(50))"))

df = pd.read_csv('address_data.csv')
# print(df)

df.to_sql('food_table', con=engine)
