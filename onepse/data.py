# OnePSE
# (Py Sdl Engine)
# by CodCatDev
# License: Apache
# https://github.com/CodCatDev/OnePSE
# 
# LocalEngine Data class

# import libs
import pathlib

# Data class for engine
class _DATA:
    # Engine version
    VERSION = "0.0.0005"
    # SDL dir
    SDL = "SDL-2.32.10"
    # Engine-Dir path
    ENGINE_PATH = pathlib.Path(__file__).resolve().parent.__str__()
    # Debug icon path
    DEBUG_ICON = f"{ENGINE_PATH}\\res\\appIcon.png"
    # Sdl path
    SDL_PATH = f"{ENGINE_PATH}\\lib\\{SDL}"
    # Standart font
    FONT_PATH = f"{ENGINE_PATH}\\res\\font.ttf"