class Shellcode(object):
	info = {
		"author" :	"",
		"credits":	"",
		"name"	 :	"",
		"references" : "",
		"platform" : "",
		"disclosureDate" : "",
		"reliability" : "",
		"rawassembly" : "",
		"size" : "",
		"payload" : "",
	}


	def getpayload(self):
		return Shellcode.info["payload"][0]


	def getsize(self,x):
		return len(x.split("\\x"))