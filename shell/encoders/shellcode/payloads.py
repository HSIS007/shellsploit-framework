class Encoders(object):
    def __init__(self):
        self.shellcode = [
            "encoders/shellcode/intel/x86/xor86.py",
            "encoders/shellcode/intel/x86/xor_b3m.py",
            "encoders/shellcode/intel/x86/xor64.py",
        ]

    def ret(self):
        return len(self.shellcode)
