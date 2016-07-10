#------------------Bombermans Team---------------------------------# 
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Shellsploit
# LICENSE : https://github.com/b3mb4m/Shellsploit/blob/master/LICENSE
#------------------------------------------------------------------#

import sys
import os
import readline


class autocomplete(object):

    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        response = None
        if state == 0:
            if text:
                self.matches = [s 
                                for s in self.options
                                if s and s.startswith(text)
                                ]
            else:
                self.matches = self.options[:]

        try:
            response = self.matches[state]
        except IndexError:
            response = None
        return response


def completion(control=False):
    if control == "shellsploit":
        from .db import shellsploitlist
        readline.set_completer(autocomplete(shellsploitlist()).complete)
        readline.parse_and_bind('tab: complete')

    elif control == "shellcodes":
        from .db import shellcodelist
        readline.set_completer(autocomplete(shellcodelist()).complete)
        readline.parse_and_bind('tab: complete')

    elif control == "injectors":
        from .db import injectorlist
        readline.set_completer(autocomplete(injectorlist()).complete)
        readline.parse_and_bind('tab: complete')

    elif control == "backdoors":
        from .db import backdoorlist
        readline.set_completer(autocomplete(backdoorlist()).complete)
        readline.parse_and_bind('tab: complete')
