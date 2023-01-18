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


#-------------------------------------------------IP RegEx-------------------------------------------------
ip_user = input("Enter the IPv4: ")
ip_find = re.search(r"^\d{1,3}(.){1}\d{1,3}(.){1}\d{1,3}(.){1}\d{1,3}$", ip_user) 
try:
  ip_find = ip_find.string
except:
  print("IPv4 format is not correct, try again...\n")


#-------------------------------------------------IP Location and Description-------------------------------------------------
r = requests.get('https://whatismyipaddress.com/ip/'+ip_find)
source = r.text
ip_location = ""

ip_desc = ""

#-------------------------------------------------Number of rows-------------------------------------------------
table_name = "blacklist"
cursor.execute("select count(*) from "+table_name)
numberOfRecords = cursor.fetchone()[0]


#-------------------------------------------------DATABASE COMMAND-------------------------------------------------
query = ("INSERT INTO " + table_name +
        "(id, ipv4, location, description) "
        " VALUES (%s, %s, %s, %s)")

pid = numberOfRecords+1
ipv4 = ip_find
location = ip_location  
description = ip_desc

#cursor.execute(query, (pid, ipv4, location, description))
#cnx.commit()


cursor.close()
cnx.close()



#country_list = "('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Austria', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Cote dIvoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'DR Congo', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faeroe Islands', 'Finland', 'France', 'French Guiana', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Réunion', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'State of Palestine', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'The Bahamas', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe')"
