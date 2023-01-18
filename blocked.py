
def ip_user():
	ip_user = input("Enter the IPv4: ")
	ip_find = re.search(r"^\d{1,3}(.){1}\d{1,3}(.){1}\d{1,3}(.){1}\d{1,3}$", ip_user) 
	try:
	  ip_find = ip_find.string
	except:
	  print("IPv4 format is not correct, try again...\n")
