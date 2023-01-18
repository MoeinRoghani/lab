import mysql.connector
import re
import requests
#from bs4 import BeautifulSoup
#https://regex101.com/

print("\nConnecting to DATABASE...\n")
config = {
  'user': 'root',
  'password': '#Private#SQL',
  'host': '127.0.0.1',
  'database': 'ssh_blocked',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
print("--------------------------Connection Stablished--------------------------\n")


