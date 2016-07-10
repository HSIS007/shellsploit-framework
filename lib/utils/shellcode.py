class ShellcodeList(object):
    @staticmethod
    def readlist():
        return [
            "linux/read",
            "freebsd_x86/read",
            "linux86/read",
            "solarisx86/read",
            "linux86/chmod",
            "linux64/read",
            "linux_arm/chmod",
            "linux_mips/chmod",
        ]


    @staticmethod
    def spawnlist():
        return [
            "linux/binsh_spawn",
            "bsdx64/binsh_spawn",
            "linux86/binsh_spawn",
            "linux_arm/binsh_spawn",
            "linux_mips/binsh_spawn",
            "osx64/binsh_spawn",
            "linux64/binsh_spawn",
            "freebsd_x86/binsh_spawn",
            "solarisx86/binsh_spawn",
            "osx86/binsh_spawn",
        ]

    @staticmethod
    def tcpbindlist():
        return [
            "linux86/tcp_bind",
            "linux64/tcp_bind",   
            "linux/tcp_bind",
            "osx64/tcp_bind",
            "solarisx86/tcp_bind",
            "linux_mips/tcp_bind",
            "osx86/tcp_bind",
            "windows/tcp_bind",
            "freebsd_x86/tcp_bind",
            "freebsd_x64/tcp_bind",
        ]

    @staticmethod
    def reversetcplist():
        return [
            "windows/reverse_tcp",
            "linux86/reverse_tcp",
            "linux64/reverse_tcp",
            "linux/reverse_tcp",
            "osx86/reverse_tcp",
            "osx64/reverse_tcp",
            "solarisx86/reverse_tcp",
            "freebsd_x86/reverse_tcp",
            "freebsd_x86/reverse_tcp2",
            "freebsd_x64/reverse_tcp",     
            "linux_mips/reverse_tcp",
            "linux_arm/reverse_tcp",
        ]


    @staticmethod
    def execlist():
        return [
            "linux86/exec",
            "freebsd_x86/exec",
            "freebsd_x64/exec",
            "linux_arm/exec",
            "windows/exec",
        ]

    @staticmethod
    def downloadandexecutelist():
        return [
            "linux86/download&exec",
            "windows/download&execute",
        ]

    @staticmethod
    def messageboxlist():
        return [
            "windows/messagebox",
        ]

    @staticmethod
    def bfdlist():
        return [
            "injectors/Windows/BFD/Patching",
            "injectors/MacOSX/BFD/Patching",
            "injectors/Linux/BFD/Patching",
            "injectors/Linux/ARM/x86/BFD/Patching",
            "injectors/FreeBSD/x86/BFD/Patching",
        ]
