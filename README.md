#Shellsploit 

[![Join the chat at https://gitter.im/b3mb4m/shellsploit-framework](https://badges.gitter.im/b3mb4m/shellsploit-framework.svg)](https://gitter.im/b3mb4m/shellsploit-framework?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
![MIT Licence](https://img.shields.io/badge/Licence-MIT_Licence-red.svg?style=plastic)
[![Python 3.4](https://img.shields.io/badge/Python-3.4-yellow.svg?style=plastic)](https://www.python.org/)
[![Python 2.7](https://img.shields.io/badge/Python-2.7-yellow.svg?style=plastic)](https://www.python.org/)
![v0.3](https://img.shields.io/badge/Release-v0.3-orange.svg?style=plastic)

-------------

Shellsploit let's you generate customized shellcodes, backdoors, injectors for various operating system.
And let's you obfuscation every byte via encoders.


#Shellsploit Wiki 
-------------------
* [Installation Guide](https://github.com/b3mb4m/shellsploit-framework/wiki/Installation-Guide)
* [Compatible Operation Systems](https://github.com/b3mb4m/shellsploit-framework/wiki/Compatible-Operation-Systems)


#Usage
-----

    usage: shellsploit  [-l] [-p] [-o] [-n]
    						[--host] [--port]


    optional arguments:
	  	   -l, --list 			Show  list of backdoors,shellcodes,encoders,injectors
	  	   -p, --payload 		Set payload for usage
	  	   -n, -nc 				Declare netcat for usage
	  	   --host				The connect/listen address
	  	   --port				The connect/listen port	

  	Inline arguments:

  		Main Menu:
			help           		Help menu
			os					Command directly ur computer
			use 				Select Module For Use
			clear				Clear the menu
			show modules    	Show Modules of Current Database
			show backdoors    	Show Backdoors of Current Database
			show injectors		Show Injectors(Shellcode,dll,so etc..)

		Shellcode Menu:
			back				Exit Current Module
			set 				Set Value Of Options To Modules
			ip					Get IP address(Requires net connection)
			os					Command directly ur computer
			clear				Clear the menu
			disas				Disassembly the shellcode(Support : x86/x64)
			whatisthis      	Learn which kind of shellcode it is
			iteration			Encoder iteration time
			generate 			Generate shellcode 
			output 				Save option to shellcode(txt,py,c,cpp,exe)
			show encoders		List all obfucscation encoders
			show options		Show Current Options Of Selected Module

		Injector Menu:
			set 				Set Value Of Options To Modules
			help 				Help menu
			back				Exit Current Module
			os  				Command directly ur computer
			pids				Get PID list of computer
			getpid				Get specific PID on list(Ex. getpid Python)


#Bugs
------

Please do not forget to report bugs! You can submit an issue, pull request, or you can pm via email or xmpp and newly gitter,


######https://gitter.im/b3mb4m/shellsploit-framework
######shellsploit-framework@exploit.im     - Instant chat
######shellsploit-framework@protonmail.com 




#Donations
-----------

Shellsploit project is completely funded  through donations(no sponsors etc.).This project consume a lot of time so if you consider worth it, please consider donation.Thank you.

BTC :  1DGrZ5BuzMAHa4dtScsSQNRXnLafnYeqqD
