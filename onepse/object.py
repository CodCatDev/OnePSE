import sdl2 as sdl
from Onepse.color import ColorObj

class Objects:
    class Rect:
        def __init__(self,width: int,height:int) -> None:
            self.width = width
            self.height = height
            self.__rect = sdl.SDL_Rect(w=width,h=height,x=300,y=200)
            self.type = "rect"
            self.color = (255,255,255)
        def setColor(self, color: ColorObj):
            self.color = (color.r,color.g,color.b)
        def _type(self):
            return self.type
        def _getRect(self):
            return self.__rect
        def _getColor(self):
            return self.color