class Encoders(object):
    def __init__(self):
        self.py = [
            'encoders/py/bzip2',
            "encoders/py/gzip",
        ]

    def ret(self):
        return len(self.py)
