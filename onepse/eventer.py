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
from onepse.res.keys import keys

# initialize a sdlExt
sdlext.init()

class KeysHandler:
    def __init__(self,keys):
        self.__keys = keys
    def key(self, key: str):
        k = key.lower()
        if k in self.__keys:
            return True
        else: 
            return False

# input handler
class EventHandler:
    def __init__(self) -> None:
        self.events = []
        self.keys = []
        self.close = False
    # update a data of events and buttons
    def updateEvents(self):
        evs = sdlext.get_events()
        for event in evs:
            if event.type == sdl.SDL_QUIT:
                self.close = True
    def updateKeys(self):
        LKey = []
        Klist = sdl.SDL_GetKeyboardState(None)
        for code, name in keys.items():
            if Klist[code]:
                LKey.append(name.lower())
        sdl.SDL_Delay(10)
        return KeysHandler(LKey)
    # Check a closing of app
    def isClose(self):
        """Return a bool value, """
        if self.close: return True
        else: return False
    def resetClosing(self): self.close = False