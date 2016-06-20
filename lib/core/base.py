from commands import Commands


class Base(Commands):
	def __init__(self):
		Commands.__init__(self)  
	
	@staticmethod
	def dynamicimport( script):
		"return a function or class"
		import importlib
		return importlib.import_module( script)


	@staticmethod
	def binary2hex( binary):
		"convert binary to hexdecimal"
		import binascii
		return binascii.hexlify(binary)


	@staticmethod
	def prettyout( shellcode):
		"Format long shellcodes"
		from re import findall
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




