# OnePSE
# (Py Sdl Engine)
# by CodCatDev
# License: Apache
# https://github.com/CodCatDev/OnePSE
# 
# Event/Input handler

# import sdl
import sdl2 as sdl
import sdl2.ext as sdlext

# import typing for List
from typing import List

# import keys list
from Onepse.res.keys import keys

# initialize a sdlExt
sdlext.init()

class InputKey:
    """Inputted key class
    

    ## Variables:
        **code** - Int value, Symbol code of the key
        **key** - String value, it's a pressed key. (Template: "W")"""
    def __init__(self, code, name):
        self.code = code
        self.key = name

# input handler
class EventHandler:
    def __init__(self) -> None:
        self.events = []
        self.keys = []
        self.close = False
    # update a data of events and buttons
    def update(self):
        """Updating a events"""
        evs = sdlext.get_events()
        for event in evs:
            if event.type == sdl.SDL_KEYDOWN and event.key.keysym.sym in keys:
                self.keys.append(event.key.keysym)
            if event.type == sdl.SDL_QUIT:
                self.close = True
    # Check a closing of app
    def isClose(self):
        """Return a bool value, """
        if self.close: return True
        else: return False
    def resetClosing(self): self.close = False
    def getKeys(self) -> List[InputKey]:
        """Return a pressed keys, as InputKey class

        Every InputKey object is a class with Key name and code.

        Returns:
            List[InputKey]: Every list value is a InputKey class."""
        Klist = []
        for key in self.keys:
            Klist.append(InputKey(key.sym, keys[key.sym]))
        self.keys = []
        return Klist
    