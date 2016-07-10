#------------------Bombermans Team---------------------------------#
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from header import *


def RawFile( shellcode):
    sc = unhexlify(shellcode.replace("\\x", ""))
        logs( sc, None)
