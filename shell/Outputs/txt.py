#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from header import *

def TxtFile( shellcode):
    db = '''#Project : https://github.com/b3mb4m/Shellsploit
#This file created with shellsploit ..
#{0} - {1}


{2}
 
'''.format(strftime("%d/%m/%Y"), strftime("%H:%M:%S"), shellcode)

    logs( db, "txt")
