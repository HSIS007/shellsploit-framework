#!/usr/bin/env python

#------------------Bombermans Team---------------------------------#
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from .control import *
from .core.logo.logo import banner
from .core.logo.counter import *
from .core.Comp import tab
from shutil import move
from lib.core.base import Base 
from sys import version_info


if version_info.major >= 3:
    raw_input = input

tab.completion( "shellsploit")
db = B3mB4mLogo().start()
def start():
    print (banner( db[0], db[1], db[2], db[3]+5))
    shellsploit().startmain()



class shellsploit(Base):
    def __init__(self):
        Base.__init__(self)   


    def startmain(self):
        try:
            bash =  bcolors.OKBLUE + bcolors.UNDERLINE + "ssf" + bcolors.ENDC
            bash += bcolors.OKBLUE + " > "+ bcolors.ENDC
            terminal = raw_input(bash)
        except KeyboardInterrupt:
            shellsploit.exit("\n[*] (Ctrl + C ) Detected, Trying To Exit ...")


        if terminal[:4] == "help" or terminal[:1] == "?":
            from .core.help import mainhelp
            mainhelp()

        elif terminal[:14] == "show backdoors":
            from .core.backdoors import backdoorlist
            backdoorlist()

        elif terminal[:13] == "show encoders":
            from .core.backdoors import encoderlist
            encoderlist()

        elif terminal[:2] == "os":
            shellsploit.oscommand( terminal[3:])

        elif terminal[:6] == "banner":
            print (banner( db[0], db[1], db[2], db[3]+5))

        elif terminal[:3] == "use":
            all_sc_modules = []
            for platforms in shellsploit.AllModules().keys():
                for shellcodeType in shellsploit.AllModules()[platforms]:
                    all_sc_modules.append("{}/{}".format(platforms,shellcodeType))
                    if terminal.split()[1] in all_sc_modules:
                        for shellcode in all_sc_modules:
                            if terminal.split()[1] == shellcode:
                                B3mB4m().control(shellcode)
                                self.startmain()
                        shellsploit.invalidcommand()
                        self.startmain()
                    #else:
                    #	shellsploit.invalidcommand()
                    #	self.startmain()


        elif terminal[:14] == "show injectors":
            from .core.lists import injectorlist
            injectorlist()

        elif terminal[:5] == "clear":
            shellsploit.clean()

        elif terminal[:15] == "show shellcodes":
            from .core.shellcodes import shellcodelist
            shellcodelist()

        elif terminal[:4] == "exit":
            shellsploit.exit("\nThanks for using shellsploit !\n")

        else:
            if not terminal:
                self.startmain()
            else:
                print (bcolors.RED + bcolors.BOLD + "[-] Unknown command: %s" % terminal + bcolors.ENDC)
                self.startmain()
        self.startmain()

def main():
    from shell.parser import Parser
    start()
