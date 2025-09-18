# OnePSE
# (Py Sdl Engine)
# by CodCatDev
# License: Apache
# https://github.com/CodCatDev/OnePSE
# 
# Window class

# import libs
import os
import pathlib

# import a data
from onepse.data import _DATA as data

# Set a SDL2.dll path
os.environ["PYSDL2_DLL_PATH"] = data.SDL_PATH

# import SDL and SDL.EXT
import sdl2 as sdl
import sdl2.ext as sdlext

# Window Create class
class CreateWindow:
    "Creating a window on the screen"
    # Create a window
    def __init__(self,title="OnePSE App",size=(600,300)) -> None:
        sdlext.init()
        self.window = sdlext.Window(title=title, size=size)
        surface = sdlext.load_image(data.DEBUG_ICON)
        sdl.SDL_SetWindowIcon(self.window.window, surface)
        sdl.SDL_FreeSurface(surface)
        self.visible = False
    # Show window
    def Show(self) -> bool:
        try:
            self.window.show()
            self.visible = True
        except:
            return False
        return True
    # Hide window
    def Hide(self) -> bool:
        try:
            self.window.hide()
            self.visible = False
        except:
            return False
        return True
    # check, if window visible?
    def IsVisible(self) -> bool: return self.visible