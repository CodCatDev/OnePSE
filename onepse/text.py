# OnePSE
# (Py Sdl Engine)
# by CodCatDev
# License: Apache
# https://github.com/CodCatDev/OnePSE
# 
# Text Class

from typing import List

class TextObject:
    def __init__(self, text: str, size: int =16, color: List[int]=[255,255,255], pos: List[int] = [300,200]):
        