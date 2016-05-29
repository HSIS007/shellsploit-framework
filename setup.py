from optparse import OptionParser
from os import system
from os import path
from os import unlink
from sys import exit
from os import sep



if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('-s', '--setup', action="store")
	parser.add_option('--user', action="store_true")
	options, args = parser.parse_args()

	if not options.setup:
		exit("\n\tUsage : setup.py -s/--setup install or uninstall ..\n")
	else:
		if options.setup == 'install':
			if options.user:
				system('python easyinstall.py install --record shellsploit.ini --user')
			else:
				system('python easyinstall.py install --record shellsploit.ini')
			

			with open("shellsploit.ini", "r") as mypath:
				for line in mypath:
					line = line.strip()
					if line.split(sep)[-2] == "shell":
						shellsploitpath = sep.join(line.strip().split(sep)[:len(line.strip().split(sep))-1])
					if "core"+sep+"logo"+sep+"counter.pyc" in line:
						unlink(line)
					if "core"+sep+"logo"+sep+"counter.py" in line and not "core"+sep+"logo"+sep+"counter.pyc" in line:
						counterpath = line

				with open(counterpath, "r+") as universal:
					data  = universal.read().replace("SHELLSPL0ITMASTERS", shellsploitpath)
					with open(counterpath, "w") as finish:
						finish.write(data)
						finish.close()

		elif options.setup == 'uninstall': 
			if not path.isfile('shellsploit.ini'):
				exit('\n\tIf you want uninstall you must install it first.\n')
			else:
				files = open('shellsploit.ini', 'r').readlines()
				unlink('shellsploit.ini')
				print ('')
				for x in files:
					if path.isfile(x.strip()):
						print ('Remove : {0}').format(x.strip()) 
						unlink(x.strip())
				else:
					exit('\nUninstall complate ! \n')

		else:
			exit("\n\tUsage : setup.py -s/--setup install or uninstall ..\n")	
