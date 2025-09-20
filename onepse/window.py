# OnePSE
# (Py Sdl Engine)
# by CodCatDev
# License: Apache
# https://github.com/CodCatDev/OnePSE
# 
# Window class

# import libs
import os

# import a data
from Onepse.data import _DATA as data

# import Typing
from typing import List

# Set a SDL2.dll path
os.environ["PYSDL2_DLL_PATH"] = data.SDL_PATH

# import SDL and SDL.EXT
import sdl2 as sdl
import sdl2.ext as sdlext

# Window Create function
def CreateWindow(title: str, size: List[int] = [600,300]):
    """Creating a Window of your application
    
    Returns:
        Class "Window", with a Data of the app"""
    return Window(title,size[0],size[1])
    
# Window class
class Window:
    def __init__(self,title: str ,width: int, height: int ) -> None:
        sdlext.init()
        self.window = sdlext.Window(title=title, size=(width, height))
        surface = sdlext.load_image(data.DEBUG_ICON)
        sdl.SDL_SetWindowIcon(self.window.window, surface)
        sdl.SDL_FreeSurface(surface)
        self.visible = False
        self._render = sdlext.Renderer(self.window)
    # Show window
    def show(self) -> bool:
        """Showing a window"""
        try:
            self.window.show()
            self.visible = True
        except:
            return False
        return True
    # Hide window
    def hide(self) -> bool:
        try:
            self.window.hide()
            self.visible = False
        except:
            return False
        return True
    # check, if window visible?
    def isVisible(self) -> bool: 
        """Return Bool value, True if window visible (show)"""
        return self.visible
    def setBgColor(self, rgb: List[int]) -> None:
        self._render.clear(sdlext.Color(rgb[0],rgb[1],rgb[2]))
    def updateRender(self) -> None:
        self._render.present()