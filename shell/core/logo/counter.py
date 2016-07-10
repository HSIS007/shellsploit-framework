#------------------Bombermans Team---------------------------------#
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Shellsploit
# LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


from os import getcwd
from os import sep
from os import walk
from sys import platform
from sys import exec_prefix
from sys import version_info
from shell.encoders.py.payloads import *
addEncoder = Encoders().ret()
from shell.encoders.shellcode.payloads import *
addEncoder += Encoders().ret()


class B3mB4mLogo(object):

    def __init__(self):
        self.db = ["database", "OS", "encoders", "inject"]
        self.ret = []
        self.control = False
        self.magic = r"SHELLSPL0ITMASTERS"
        self.ignore = ["BFDBackdoors", "pyminifier", "__pycache__"]
        self.decide = False

    def calculate(self, select, files=True):
        if files == True:
            self.cout = 0
            for root, dirs, files in walk(self.magic + sep + select, topdown=True):
                for x in files:
                    if ".pyc" not in x and "__" not in x and ".md" not in x:
                        if select == "inject":
                            if "inject" in x.lower():
                                self.cout += 1
                        else:
                            if not x.endswith(".pyc"):
                                if select == "encoders":
                                    continue
                                else:
                                    self.cout += 1

            # ret function for encoders ..
            return self.cout + addEncoder if select == "encoders" else self.cout

        else:
            self.cout = 0
            for root, dirs, files in walk(self.magic + sep + select, topdown=True):
                if dirs in self.ignore:
                    continue	
                for x in dirs:
                    if "__" not in x:
                        self.cout += 1
            return self.cout

    def start(self):
        for x in self.db:
            if x != "OS":
                self.ret.append(self.calculate(x, True))
            else:
                self.ret.append(self.calculate("database", False))
        return self.ret
