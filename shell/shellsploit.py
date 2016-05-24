#!/usr/bin/env python

#------------------Bombermans Team---------------------------------#
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import sys
import os
import time

name = os.sep.join([x for x in os.getcwd().split(os.sep) if x != os.getcwd().split(os.sep)[-1]])
sys.path.append(name)

if sys.version_info.major >= 3:
    raw_input = input


from .control import *
from .core.logo.logo import banner
from .core.logo.counter import *
from .core.Comp import tab
from shell.payloads import *
from shutil import move


tab.completion( "shellsploit")
db = B3mB4mLogo().start()
def start():
	print (banner( db[0], db[1], db[2], db[3]+5))
	shellsploit()

def inform( payload):
	print 


def shellsploit():
	try:
		bash =  bcolors.OKBLUE + bcolors.UNDERLINE + "ssf" + bcolors.ENDC
		bash += bcolors.OKBLUE + " > "+ bcolors.ENDC
		terminal = raw_input(bash)
	except KeyboardInterrupt:
		sys.exit("\n[*] (Ctrl + C ) Detected, Trying To Exit ...")


	if terminal[:4] == "help" or terminal[:1] == "?":
		from .core.help import mainhelp
		mainhelp()
		shellsploit()

	elif terminal[:14] == "show backdoors":
		from .core.backdoors import backdoorlist
		backdoorlist()
		shellsploit()

	elif terminal[:13] == "show encoders":
		from .core.backdoors import encoderlist
		encoderlist()
		shellsploit()


	elif terminal[:2] == "os":
		from .core.commands import oscommand
		oscommand( terminal[3:])
		shellsploit()


	elif terminal[:6] == "banner":
		print (banner( db[0], db[1], db[2], db[3]+5))
		shellsploit()

	elif terminal[:3] == "use":
		all_sc_modules = []
		for platforms in shellcodeModules.keys():
			for shellcodeType in shellcodeModules[platforms]:
				all_sc_modules.append("{}/{}".format(platforms,shellcodeType))
				if terminal.split()[1] in all_sc_modules:
					for shellcode in all_sc_modules:
						if terminal.split()[1] == shellcode:
							B3mB4m().control(shellcode)
							shellsploit()

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

	elif terminal[:15] == "show shellcodes":
		from .core.shellcodes import shellcodelist
		shellcodelist()
		shellsploit()



	elif terminal[:4] == "exit":
		sys.exit("\nThanks for using shellsploit !\n")

	else:
		if not terminal:
			shellsploit()
		else:
			print (bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC)
			shellsploit()


def main():
	import optparse
	parser = optparse.OptionParser()
	parser.add_option('-p', '--payload', action="store")
	parser.add_option('-e', '--encoder', action="store", default="False")
	parser.add_option('-l','--list', action="store", default=True)
	parser.add_option('-n','--nc', action="store", default=True)

	#External sources(shellcode,py,asm encoders etc.)
	parser.add_option('-s', '--script', action="store")
	parser.add_option('-o', '--output', action="store", default=False)
	parser.add_option('-i', '--iteration', action="store")


	#Commandline shellcodes
	parser.add_option('--host', action="store")
	parser.add_option('--port', action="store")
	parser.add_option('--shellcode', action="store")
	parser.add_option('--url', action="store")
	parser.add_option('--message', action="store")
	parser.add_option('--file', action="store")
	parser.add_option('--filename', action="store")
	parser.add_option('--password', action="store")
	parser.add_option('--command', action="store")
	(options, args) = parser.parse_args()


	if options.list == "backdoors":
		from .core.backdoors import backdoorlist
		backdoorlist( require=False)
		sys.exit()


	if options.list == "shellcodes":
		from .core.shellcodes import shellcodelist
		shellcodelist()
		sys.exit()


	if options.list == "encoders":
		from .core.backdoors import encoderlist
		encoderlist( require=False)
		sys.exit()


	if options.shellcode:
		from .core.shellcodes import shellcodelist
		shellcodelist = [x.lower() for x in shellcodelist( True)]
		if options.shellcode.lower() in shellcodelist:
			from .database.generator import generator
			choose, shellcode = options.shellcode.split("/")
			startime = time.time()
			output = ("\n"+generator( 
				choose=choose, shellcode=shellcode, COMMAND=options.command,
				FILE=options.file, FILENAME=options.filename, ip=options.host,
				port=options.port, URL=options.url, PASSWORD=options.password
			)+"\n\n")

			print ("\nModule : {0}".format(options.shellcode))
			print ("Generate time : %.2f" % (float(startime)-(time.time())))
			print (output)
		sys.exit()


	if options.list == "injectors":
		from .core.lists import injectorlist
		injectorlist()
		sys.exit()

	elif options.nc == "netcat" or options.nc == "nc":
		from .Session.netcat import nc
		if options.port:
			nc( int(options.port))
		else:
			nc()
		sys.exit()


	else:
		if options.payload:
			if options.host and options.port:
				from .core.backdoors import backdoorlist
				from .core.backdoors import encoderlist
				if options.payload in backdoorlist( require=True):
					from .Session.generator import process
					if options.encoder in encoderlist( True):
						if "py" in options.encoder and "python" not in options.payload:
							sys.exit("\nThis encoder can not use with that payload\n")
						if options.output:
							process( options.payload, options.host, options.port, options.encoder, options.output)
						else:
							process( options.payload, options.host, options.port, options.encoder,True)
				else:
					sys.exit("\npython shellsploit  -p PAYLOAD -e ENCODER --host IP --port P0RT\n")
			else:
				sys.exit("\npython shellsploit  -p PAYLOAD -e ENCODER --host IP --port P0RT\n")


		#For external scripts
		elif options.script:
			if options.encoder:
				from .core.backdoors import encoderlist
				if options.encoder in encoderlist( True):
					if "/py/" in options.encoder:
						from shell.encoders.py.starter import control
					elif "/shellcode/" in options.encoder:
						from shell.encoders.shellcode.starter import control
					#elif options.script.endswith(".py") and "/py/" in options.encoder:
					#elif options.script.endswith(".py") and "/py/" in options.encoder: 
					try:
						options.script = os.getcwd()+os.sep+options.script if "/" not in options.script else options.script
						control(payload=options.encoder, files=[options.script], iteration=options.iteration)
						if options.output:
							if os.path.isdir("/".join(options.output.split("/")[:(len(options.output.split("/"))-1)])):
								try:
									move(options.script, options.output)
								except Exception as error:
									sys.exit( "\nUnexpected error while moving file to target\n")
								else:
									sys.exit("\nFile encoded  : {0}\n".format( options.output)) 
							else:
								sys.exit("\nYour target directory is not exist.\n")
						else:
							sys.exit("\nFile encoded  : {0}\n".format( options.script))	
					except Exception as error:
						sys.exit("\nUnexpected error : {0}\n".format( error))
				else:
					sys.exit("\npython shellsploit  --script YOURFILE --encoder ENCODERNAME\n")
			else:
				sys.exit("\npython shellsploit  --script YOURFILE --encoder ENCODERNAME\n")	
	start()
