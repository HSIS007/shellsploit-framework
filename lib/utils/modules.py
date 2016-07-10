from lib.utils.shellcode import ShellcodeList


class modulelist(ShellcodeList):

    def __init__(self):
        ShellcodeList.__init__(self)

    @staticmethod
    def AllModules():
        return {
            "linux86":
            [
                "binsh_spawn",
                "read",
                "exec",
                "chmod",
                "tcp_bind",
                "reverse_tcp",
                "download&exec"
            ],

            "linux64":
            [
                "read",
                "binsh_spawn",
                "tcp_bind",
                "reverse_tcp"
            ],

            "linux":
            [
                "binsh_spawn",
                "tcp_bind",
                "reverse_tcp",
                "read"
            ],

            "osx86":
            [
                "tcp_bind",
                "binsh_spawn",
                "reverse_tcp"
            ],

            "osx64":
            [
                "reverse_tcp",
                "tcp_bind",
                "binsh_spawn"
            ],

            "FreeBSDx86":
            [
                "binsh_spawn",
                "reverse_tcp",
                "read", "exec",
                "tcp_bind"
            ],
            "FreeBSDx64":
            [
                "binsh_spawn",
                "tcp_bind",
                "reverse_tcp",
                "exec"
            ],

            "linux_arm":
            [
                "binsh_spawn",
                "chmod",
                "reverse_tcp",
                "exec"
            ],

            "linux_mips":
            [
                "binsh_spawn",
                "chmod",
                "reverse_tcp",
                "tcp_bind"
            ],

            "windows":
            [
                "messagebox",
                "download&execute",
                "exec",
                "reverse_tcp",
                "tcp_bind"
            ],

            "solarisx86":
            [
                "binsh_spawn",
                "read",
                "reverse_tcp",
                "tcp_bind"
            ],

            "injectors":
            [
                "Linux/x86/ptrace",
                "Linux64/ptrace",
                "Windows/x86/tLsInjectorDLL",
                "Windows/x86/CodecaveInjector",
                "Windows/Dllinjector",
                "Windows/BFD/Patching",
                #"MacOSX/BFD/Patching",
                #"Linux/BFD/Patching",
                #"Linux/ARM/x86/BFD/Patching",
                #"FreeBSD/x86/BFD/Patching",
            ],

            "backdoors":
            [
                "linux86/reverse_tcp",
                "linux64/reverse_tcp",
                "osx86/reverse_tcp",
                "unix/python/reverse_tcp",
                "unix/perl/reverse_tcp",
                "unix/bash/reverse_tcp",
                "unix/ruby/reverse_tcp",
                "windows/asm/reverse_tcp",
                "windows/ps/reverse_tcp",

            ],

            "encoders":
            [
                "py/bzip2",
                "py/gzip",
                "shellcode/intel/xor86.py",
                "shellcode/intel/x86/xor_b3m.py",
                #"shellcode/intel/x86/xor64.py",
            ],
        }
