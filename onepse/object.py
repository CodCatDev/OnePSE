import sdl2 as sdl
import sdl2.ext as sdlext
from onepse.color import ColorObj
from onepse.data import _DATA
sdlext.ttf._ttf_init()
class Objects:
    class Rect:
        def __init__(self,width: int,height:int) -> None:
            self.__width = width
            self.__height = height
            self.__x = 0
            self.__y = 0
            self.__rect = sdl.SDL_Rect(w=width,h=height,x=self.__x,y=self.__y)
            self.__type = "rect"
            self.__color = (255,255,255)
        def setColor(self, color: ColorObj) -> None:
            self.__color = (color.r,color.g,color.b)
        def _type(self) -> str:
            return self.__type
        def _getRect(self) -> sdl.SDL_Rect:
            return self.__rect
        def _getColor(self) -> tuple:
            return self.__color
        def getPos(self) -> list:
            return [self.__x, self.__y]
        def setPos(self, x: int, y: int) -> None:
            self.__x = x
            self.__y = y
            self.__rect.x = x
            self.__rect.y = y
        def changePos(self,xto:int = 0,yto:int = 0) -> None:
            x,y = self.__x,self.__y
            x += xto
            y += yto
            self.__x = x
            self.__y = y
            self.__rect.x = x
            self.__rect.y = y

class Text:
    def __init__(self,text: str, size: int = 16, color: ColorObj = ColorObj(255,255,255)):
        self.__text = sdlext.FontTTF(font={_DATA.FONT_PATH}, size=size,color=(color.r,color.b,color.g))