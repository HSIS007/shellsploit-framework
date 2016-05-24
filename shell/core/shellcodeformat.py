#------------------Bombermans Team---------------------------------#
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


from re import findall

def prettyout( shellcode):
	data = shellcode.replace("\\x", "")
	db = []
	print ("\n")
	for x in [data[x:x+40] for x in range(0, len(data), 40)]:
		db = findall("..?", x)
		if data.endswith( x):
			print ('\t"\\x'+"\\x".join(db)+'"')
		else:
			print ('\t"\\x'+"\\x".join(db)+'"'+' +')
	print ("\n")
	
