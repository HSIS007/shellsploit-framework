#!/usr/bin/env python

#------------------Bombermans Team---------------------------------#
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import sys
import os

name = os.sep.join([x for x in os.getcwd().split(os.sep) if x != os.getcwd().split(os.sep)[-1]])
sys.path.append(name)

if sys.version_info.major == 3:
        raw_input = input


from .control import *
from .core.logo.logo import banner
#from .core.logo.counter import * #- Will be  improved(buggy)
#Dynamic counter for shellcodes,injectors etc..
from .core.Comp import tab


tab.start(1)
#db = B3mB4mLogo().start()
def start():
	print (banner( "47", "12", "2", "3"))
	shellsploit()

def shellsploit():
	try:
		bash =  bcolors.OKBLUE + bcolors.UNDERLINE + "ssf" + bcolors.ENDC
		bash += bcolors.OKBLUE + " > "+ bcolors.ENDC
		#terminal = raw_input(bash).lower()
		try:
			terminal = raw_input(bash)
		except EOFError, KeyboardInterrupt:
                        return

		if terminal[:4] == "help":
			from .core.help import mainhelp
			mainhelp()
			shellsploit()

		elif terminal[:14] == "show backdoors":
			from .core.backdoors import backdoorlist
			backdoorlist()
			shellsploit()

		elif terminal[:2] == "os":
			from .core.commands import oscommand
			oscommand( terminal[3:])
			shellsploit()


		elif terminal[:6] == "banner":
			print (banner( "47", "12", "2", "3"))
			shellsploit()

		elif terminal[:3] == "use":
			if terminal[4:len("linux86/binsh_spawn")+4] == "linux86/binsh_spawn":
				B3mB4m().control( "linux86/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux86/read")+4] == "linux86/read":
				B3mB4m().control( "linux86/read")
				shellsploit()
			elif terminal[4:len("linux86/chmod")+4] == "linux86/chmod":
				B3mB4m().control( "linux86/chmod")
				shellsploit()
			elif terminal[4:len("linux86/tcp_bind")+4] == "linux86/tcp_bind":
				B3mB4m().control( "linux86/tcp_bind")
				shellsploit()
			elif terminal[4:len("linux86/reverse_tcp")+4] == "linux86/reverse_tcp":
				B3mB4m().control( "linux86/reverse_tcp")
				shellsploit()
			elif terminal[4:len("linux86/exec")+4] == "linux86/exec":
				B3mB4m().control( "linux86/exec")
				shellsploit()
			elif terminal[4:len("linux86/download&exec")+4] == "linux86/download&exec":
				B3mB4m().control( "linux86/download&exec")
				shellsploit()


			elif terminal[4:len("linux64/read")+4] == "linux64/read":
				B3mB4m().control( "linux64/read")
				shellsploit()
			elif terminal[4:len("linux64/binsh_spawn")+4] == "linux64/binsh_spawn":
				B3mB4m().control( "linux64/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux64/tcp_bind")+4] == "linux64/tcp_bind":
				B3mB4m().control( "linux64/tcp_bind")
				shellsploit()
			elif terminal[4:len("linux64/reverse_tcp")+4] == "linux64/reverse_tcp":
				B3mB4m().control( "linux64/reverse_tcp")
				shellsploit()

			elif terminal[4:len("linux/binsh_spawn")+4] == "linux/binsh_spawn":
				B3mB4m().control( "linux/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux/tcp_bind")+4] == "linux/tcp_bind":
				B3mB4m().control( "linux/tcp_bind")
				shellsploit()
			elif terminal[4:len("linux/reverse_tcp")+4] == "linux/reverse_tcp":
				B3mB4m().control( "linux/reverse_tcp")
				shellsploit()
			elif terminal[4:len("linux/read")+4] == "linux/read":
				B3mB4m().control( "linux/read")
				shellsploit()



			elif terminal[4:len("osx86/tcp_bind")+4] == "osx86/tcp_bind":
				B3mB4m().control( "osx86/tcp_bind")
				shellsploit()
			elif terminal[4:len("osx86/binsh_spawn")+4] == "osx86/binsh_spawn":
				B3mB4m().control( "osx86/binsh_spawn")
				shellsploit()
			elif terminal[4:len("osx86/reverse_tcp")+4] == "osx86/reverse_tcp":
				B3mB4m().control( "osx86/reverse_tcp")
				shellsploit()


			elif terminal[4:len("osx64/reverse_tcp")+4] == "osx64/reverse_tcp":
				B3mB4m().control( "osx64/reverse_tcp")
				shellsploit()
			elif terminal[4:len("osx64/tcp_bind")+4] == "osx64/tcp_bind":
				B3mB4m().control( "osx64/tcp_bind")
				shellsploit()
			elif terminal[4:len("osx64/binsh_spawn")+4] == "osx64/binsh_spawn":
				B3mB4m().control( "osx64/binsh_spawn")
				shellsploit()



			elif terminal[4:len("FreeBSDx86/binsh_spawn")+4] == "FreeBSDx86/binsh_spawn":
				B3mB4m().control( "freebsd_x86/binsh_spawn")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/reverse_tcp2")+4] == "FreeBSDx86/reverse_tcp2":
				B3mB4m().control( "freebsd_x86/reverse_tcp2")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/reverse_tcp")+4] == "FreeBSDx86/reverse_tcp":
				B3mB4m().control( "freebsd_x86/reverse_tcp")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/read")+4] == "FreeBSDx86/read":
				B3mB4m().control( "freebsd_x86/read")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/exec")+4] == "FreeBSDx86/exec":
				B3mB4m().control( "freebsd_x86/exec")
				shellsploit()
			elif terminal[4:len("FreeBSDx86/tcp_bind")+4] == "FreeBSDx86/tcp_bind":
				B3mB4m().control( "freebsd_x86/tcp_bind")
				shellsploit()


			elif terminal[4:len("FreeBSDx64/binsh_spawn")+4] == "FreeBSDx64/binsh_spawn":
				B3mB4m().control( "freebsd_x64/binsh_spawn")
				shellsploit()
			elif terminal[4:len("FreeBSDx64/tcp_bind")+4] == "FreeBSDx64/tcp_bind":
				B3mB4m().control( "freebsd_x64/tcp_bind")
				shellsploit()
			elif terminal[4:len("FreeBSDx64/reverse_tcp")+4] == "FreeBSDx64/reverse_tcp":
				B3mB4m().control( "freebsd_x64/reverse_tcp")
				shellsploit()
			elif terminal[4:len("FreeBSDx64/exec")+4] == "FreeBSDx64/exec":
				B3mB4m().control( "freebsd_x64/exec")
				shellsploit()


			elif terminal[4:len("linux_arm/binsh_spawn")+4] == "linux_arm/binsh_spawn":
				B3mB4m().control( "linux_arm/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux_arm/chmod")+4] == "linux_arm/chmod":
				B3mB4m().control( "linux_arm/chmod")
				shellsploit()
			elif terminal[4:len("linux_arm/reverse_tcp")+4] == "linux_arm/reverse_tcp":
				B3mB4m().control( "linux_arm/reverse_tcp")
				shellsploit()
			elif terminal[4:len("linux_arm/exec")+4] == "linux_arm/exec":
				B3mB4m().control( "linux_arm/exec")
				shellsploit()



			elif terminal[4:len("linux_mips/binsh_spawn")+4] == "linux_mips/binsh_spawn":
				B3mB4m().control( "linux_mips/binsh_spawn")
				shellsploit()
			elif terminal[4:len("linux_mips/chmod")+4] == "linux_mips/chmod":
				B3mB4m().control( "linux_mips/chmod")
				shellsploit()
			elif terminal[4:len("linux_mips/reverse_tcp")+4] == "linux_mips/reverse_tcp":
				B3mB4m().control( "linux_mips/reverse_tcp")
				shellsploit()
			elif terminal[4:len("linux_mips/tcp_bind")+4] == "linux_mips/tcp_bind":
				B3mB4m().control( "linux_mips/tcp_bind")
				shellsploit()

			#elif windows/reverse_tcp
			#elif windows/tcp_bind
			elif terminal[4:len("windows/messagebox")+4] == "windows/messagebox":
				B3mB4m().control( "windows/messagebox")
				shellsploit()
			elif terminal[4:len("windows/download&execute")+4] == "windows/download&execute":
				B3mB4m().control( "windows/download&execute")
				shellsploit()
			elif terminal[4:len("windows/exec")+4] == "windows/exec":
				B3mB4m().control( "windows/exec")
				shellsploit()

			elif terminal[4:len("solarisx86/binsh_spawn")+4] == "solarisx86/binsh_spawn":
				B3mB4m().control( "solarisx86/binsh_spawn")
				shellsploit()
			elif terminal[4:len("solarisx86/read")+4] == "solarisx86/read":
				B3mB4m().control( "solarisx86/read")
				shellsploit()
			elif terminal[4:len("solarisx86/reverse_tcp")+4] == "solarisx86/reverse_tcp":
				B3mB4m().control( "solarisx86/reverse_tcp")
				shellsploit()
			elif terminal[4:len("solarisx86/tcp_bind")+4] == "solarisx86/tcp_bind":
				B3mB4m().control( "solarisx86/tcp_bind")
				shellsploit()



			#elif terminal[4:len("injectors/Windows/byteman")+4] == "injectors/Windows/byteman":
				#B3mB4m().control( "injectors/Windows/byteman")
				#shellsploit()
			elif terminal[4:len("injectors/Linux86/ptrace")+4] == "injectors/Linux86/ptrace":
				B3mB4m().control( "injectors/Linux86/ptrace")
				shellsploit()
			elif terminal[4:len("injectors/Linux64/ptrace")+4] == "injectors/Linux64/ptrace":
				B3mB4m().control( "injectors/Linux64/ptrace")
				shellsploit()
			elif terminal[4:len("injectors/Windowsx86/tLsInjectorDLL")+4] == "injectors/Windowsx86/tLsInjectorDLL":
				B3mB4m().control( "injectors/Windowsx86/tLsInjectorDLL")
				shellsploit()
			#elif terminal[4:len("injectors/Windowsx86/Codecave")+4] == "injectors/Windowsx86/Codecave":
				#B3mB4m().control( "injectors/Windowsx86/Codecave")
				#shellsploit()







			elif terminal[4:len("backdoors/linux86/reverse_tcp")+4] == "backdoors/linux86/reverse_tcp":
				B3mB4m().control( "backdoors/linux86/reverse_tcp")
				shellsploit()
			elif terminal[4:len("backdoors/linux64/reverse_tcp")+4] == "backdoors/linux64/reverse_tcp":
				B3mB4m().control( "backdoors/linux64/reverse_tcp")
				shellsploit()
			elif terminal[4:len("backdoors/osx86/reverse_tcp")+4] == "backdoors/osx86/reverse_tcp":
				B3mB4m().control( "backdoors/osx86/reverse_tcp")
				shellsploit()
			#elif terminal[4:len("backdoors/windowsx86/reverse_tcp")+4] == "backdoors/windowsx86/reverse_tcp":
				#B3mB4m().control( "backdoors/windowsx86/reverse_tcp")
				#shellsploit()
			#elif terminal[4:len("backdoors/windowsx64/reverse_tcp")+4] == "backdoors/windowsx64/reverse_tcp":
				#B3mB4m().control( "backdoors/windowsx64/reverse_tcp")
				#shellsploit()

			#elif terminal[4:len("backdoors/php/reverse_tcp")+4] == "backdoors/php/reverse_tcp":
				#B3mB4m().control( "backdoors/php/reverse_tcp")
				#shellsploit()
			#elif terminal[4:len("backdoors/asp/reverse_tcp")+4] == "backdoors/asp/reverse_tcp":
				#B3mB4m().control( "asp/reverse_tcp")
				#shellsploit()
			#elif terminal[4:len("backdoors/jsp/reverse_tcp")+4] == "backdoors/jsp/reverse_tcp":
				#B3mB4m().control( "backdoors/jsp/reverse_tcp")
				#shellsploit()
			#elif terminal[4:len("backdoors/war/reverse_tcp")+4] == "backdoors/war/reverse_tcp":
				#B3mB4m().control( "backdoors/war/reverse_tcp")
				#shellsploit()

			elif terminal[4:len("backdoors/unix/python/reverse_tcp")+4] == "backdoors/unix/python/reverse_tcp":
				B3mB4m().control( "backdoors/unix/python/reverse_tcp")
				shellsploit()
			elif terminal[4:len("backdoors/unix/perl/reverse_tcp")+4] == "backdoors/unix/perl/reverse_tcp":
				B3mB4m().control( "backdoors/unix/perl/reverse_tcp")
				shellsploit()
			elif terminal[4:len("backdoors/unix/bash/reverse_tcp")+4] == "backdoors/unix/bash/reverse_tcp":
				B3mB4m().control( "backdoors/unix/bash/reverse_tcp")
				shellsploit()
			elif terminal[4:len("backdoors/unix/ruby/reverse_tcp")+4] == "backdoors/unix/ruby/reverse_tcp":
				B3mB4m().control( "backdoors/unix/ruby/reverse_tcp")
				shellsploit()






			else:
				print ("\nModule not avaible !\n")
				shellsploit()


		elif terminal[:14] == "show injectors":
			from .core.lists import injectorlist
			injectorlist()
			shellsploit()

		elif terminal[:5] == "clear":
			from .core.commands import clean
			clean()
			shellsploit()

		elif terminal[:12] == "show modules":
			from .core.shellcodes import shellcodelist
			shellcodelist()
			shellsploit()


		elif terminal[:4] == "exit":
			sys.exit("\nThanks for using shellsploit !\n")

		else:
			if terminal == "":
				shellsploit()
			else:
				print (bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC)
				shellsploit()



	except(KeyboardInterrupt):
		print("\n[*] (Ctrl + C ) Detected, Trying To Exit ...")
		from sys import exit
		sys.exit()



def main():
	import optparse
	parser = optparse.OptionParser()
	parser.add_option('-p', '--payload', action="store")
	parser.add_option('-o', '--output', action="store", default=True)
	parser.add_option('-l','--list', action="store", default=True)
	parser.add_option('-n','--nc', action="store", default=True)
	parser.add_option('--host', action="store")
	parser.add_option('--port', action="store")
	(options, args) = parser.parse_args()


	if options.list == "backdoors":
		from .core.backdoors import backdoorlist
		backdoorlist( require=False)

	elif options.nc == "netcat" or options.nc == "nc":
		from .Session.netcat import nc
		if options.port:
			nc( PORT)
		else:
			nc()
	else:
		if options.payload:
			if options.host and options.port:
				from .core.backdoors import backdoorlist
				if options.payload in backdoorlist( require=True):
					from .Session.generator import process
					if options.output:
						process( options.payload, options.host, options.port, options.output)
					else:
						process( options.payload, options.host, options.port, True)
						#Default, file will be create with random name.
				else:
					print ("\npython shellsploit  -p PAYLOAD --host IP --port P0RT\n")
			else:
				print ("\npython shellsploit  -p PAYLOAD --host IP --port P0RT\n")
		else:
			start()
