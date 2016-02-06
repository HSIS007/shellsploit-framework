def linux86ptrace( pid, shellcode):
	from .Linux86.inject import injectmex86
	injectmex86( pid, shellcode)

def linux64ptrace( pid, shellcode):
	from .Linux64.inject import injectmex64
	injectmex64( pid, shellcode)




