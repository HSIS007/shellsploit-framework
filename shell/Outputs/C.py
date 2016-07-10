#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from header import *

def CFile( shellcode):
    db = """//Project : https://github.com/b3mb4m/Shellsploit
//This file created with shellsploit ..
//%s - %s
//Compile : gcc -fno-stack-protector -z execstack shell.c -o shell

unsigned char shellcode[] = "%s";

int main(void){
	(*(void(*)()) shellcode)();
}

  
""" % (strftime("%d/%m/%Y"), strftime("%H:%M:%S"), shellcode)

    logs( db, "c")
