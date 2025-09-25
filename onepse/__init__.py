# OnePSE
# (Py Sdl Engine)
# by CodCatDev
# License: Apache
# https://github.com/CodCatDev/OnePSE
# 
# Init class

# importing all
from onepse.window import CreateWindow
from onepse.eventer import EventHandler
from onepse.color import Color
from onepse.object import Objects
from onepse.debugger import Debugger as __dbg__
from onepse.data import _DATA as __dt__

__db__ = __dbg__()
__db__.log("OnePSE", f"Welcome to OnePSE {__dt__.VERSION}!")
__db__.log("OnePSE", "Please, star project at Github!")
__db__.log("OnePSE Window", "App Debug started!")
del __db__
del __dbg__
del __dt__