# OnePSE
# (Py Sdl Engine)
# by CodCatDev
# License: Apache
# https://github.com/CodCatDev/OnePSE
# 
# Color class

class ColorObj:
    def __init__(self,r: int,g: int,b: int, hex: str = "NaN") -> None:
        self.r = r
        self.g = g
        self.b = b
        self.hex = hex

class Color:
    def __init__(self):
        pass
    def rgb(self, r: int, g: int, b: int) -> ColorObj:
        return ColorObj(r,g,b)
    def hex(self, hex:str) -> ColorObj:
        hex_color = hex.lstrip("#")
        r,g,b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return ColorObj(r,g,b,hex)