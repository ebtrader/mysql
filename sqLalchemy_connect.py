import mysql.connector
import os

from sqlalchemy import create_engine
import pandas as pd

# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

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

connection_string = 'mysql+mysqlconnector://jsiddique:suite203!@mysql.codingadventures.space/cheapcooking_db'

engine = create_engine(connection_string)


