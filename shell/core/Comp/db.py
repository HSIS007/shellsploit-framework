#------------------Bombermans Team---------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Shellsploit
# LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#


#from shell.payloads import *
from lib.utils.modules import modulelist 


def shellsploitlist():
    list = [
        "help",		
        "os",
        "use",
        "clear",
        "show",
        "shellcodes",
        "backdoors",
        "injectors",	
        "encoders",

    ]
    all_sc_modules = []
    for platforms in modulelist().AllModules().keys():
        for shellcodeType in modulelist().AllModules()[platforms]:
            all_sc_modules.append("{}/{}".format(platforms, shellcodeType))
            for shellcode in all_sc_modules:
                list.append(shellcode)
    return list


def shellcodelist():
    return [
        "back",	
        "set",			
        "unset",			
        "ip",		
        "os",			
        "clear",		
        "disas",		
        "whatisthis",      
        "iteration",	
        "generate",	
        "output", 	
        "show", 
        "encoders",	
        "options",	
        "help",
    ]


def injectorlist():
    return [
        "set",	
        "unset",			
        "help",			
        "back",		
        "os",			
        "getpid",		
        "clear",		
        "inject",      
        "iteration",	
        "show",	
        "options", 	
        "shellcode", 
    ]


def backdoorlist():
    return [
        "set",	
        "unset",			
        "help",			
        "back",		
        "os",			
        "clear",		
        "generate",      
        "show",	
        "options", 	
    ]
