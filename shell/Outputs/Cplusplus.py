#------------------Bombermans Team---------------------------------# 
#Author  : B3mB4m
#Concat  : b3mb4m@protonmail.com
#Project : https://github.com/b3mb4m/Shellsploit
#LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

from header import *

def CplusplusFile( shellcode, win=False):
    if win == True:
        db = """//Project : https://github.com/b3mb4m/Shellsploit
//This file created with shellsploit ..
//%s - %s
//Compile : gcc shell.c -o shell.exe


#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <windows.h>
		 
		 
int main(void)
{
	char *shellcode = "%s";
	DWORD why_must_this_variable;
	BOOL ret = VirtualProtect (shellcode, strlen(shellcode),
	PAGE_EXECUTE_READWRITE, &why_must_this_variable);
		 
	if (!ret) {
		printf ("VirtualProtect");
		return EXIT_FAILURE;
	}
			 
	
	((void (*)(void))shellcode)();
	return EXIT_SUCCESS;
}	

		""" % ( strftime("%d/%m/%Y"), strftime("%H:%M:%S"), shellcode)

    else:
        db = """//Project : https://github.com/b3mb4m/Shellsploit
//This file created with shellsploit ..
//%s - %s
//Compile : g++ -fno-stack-protector -z execstack shell.cpp -o shell

unsigned char shellcode[] = "%s";

int main(){
	int (*func)() = (int(*)())shellcode;   
	func();
}
		  
		""" % (strftime("%d/%m/%Y"), strftime("%H:%M:%S"), shellcode)


    logs( db, "cpp")



