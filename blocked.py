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


def ip_user():
	ip_user = input("Enter the IPv4: ")
	ip_find = re.search(r"^\d{1,3}(.){1}\d{1,3}(.){1}\d{1,3}(.){1}\d{1,3}$", ip_user) 
	try:
	  ip_find = ip_find.string
	except:
	  print("IPv4 format is not correct, try again...\n")