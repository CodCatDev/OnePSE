import time
from typing import TextIO

class Debugger:
    def __init__(self) -> None:
        self.__logData: list[str] = []
    def log(self, name: str, text: str) -> bool:
        """Logging a text in console
        
        ## Args:
            **name** - Name of process, who printing this
            **text** - Text to log in console"""
        try:
            timm = time.localtime()
            tm = f"{timm.tm_hour}:{timm.tm_min}:{timm.tm_sec}"
            text = f"[{tm}] [{name}] {text}"
            print(text)
            self.__logData.append(text)
        except:
            return False
        return True
    def warn(self, name: str, text: str) -> bool:
        """Printing a Warning in console
        
        ## Args:
            **name** - Name of process, who warning this
            **text** - Text to warn in console"""
        try:
            timm = time.localtime()
            tm = f"{timm.tm_hour}:{timm.tm_min}:{timm.tm_sec}"
            col = "\033[33m"
            res = "\033[0m"
            txt = f"{col}[{tm}] (WARN) [{name}] {text}{res}"
            logText = f"[{tm}] (WARN) [{name}] {text}"
            print(txt)
            self.__logData.append(logText)
        except:
            return False
        return True
    def err(self, name: str, text: str) -> bool:
        """Printing a Error in console
        
        ## Args:
            **name** - Name of process, who erroring this
            **text** - Text to error in console"""
        try:
            timm = time.localtime()
            tm = f"{timm.tm_hour}:{timm.tm_min}:{timm.tm_sec}"
            col = "\033[31m"
            res = "\033[0m"
            txt = f"{col}[{tm}] (ERROR) [{name}] {text}{res}"
            logText = f"[{tm}] (ERROR) [{name}] {text}"
            print(txt)
            self.__logData.append(logText)
        except:
            return False
        return True
    def getLogs(self) -> list[str]:
        """Returns a all logs in list format
        
        Every element - 1 line in logs"""
        return self.__logData
    def saveLogs(self,file: TextIO) -> None:
        """Saving logs in file"""
        text = ""
        for line in self.__logData:
            text += f"{line}\n"
        file.write(text)