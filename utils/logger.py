import logging
import sys
from typing import Optional
from enum import Enum

class LogColor(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

class VirtualAssistantLogger:
    def __init__(self, name: str = "virtual-assistant"):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            handler.setLevel(logging.DEBUG)
            self.logger.addHandler(handler)
    
    def _colored_print(self, message: str, color: LogColor, level: str = "INFO"):
        colored_message = f"{color.value}[{level}] {self.name}: {message}{LogColor.RESET.value}"
        print(colored_message)
    
    def info(self, message: str, color: Optional[LogColor] = LogColor.CYAN):
        if color:
            self._colored_print(message, color, "INFO")
        else:
            self.logger.info(f"{self.name}: {message}")
    
    def debug(self, message: str, color: Optional[LogColor] = LogColor.MAGENTA):
        if color:
            self._colored_print(message, color, "DEBUG")
        else:
            self.logger.debug(f"{self.name}: {message}")
    
    def warning(self, message: str, color: Optional[LogColor] = LogColor.YELLOW):
        if color:
            self._colored_print(message, color, "WARNING")
        else:
            self.logger.warning(f"{self.name}: {message}")
    
    def error(self, message: str, color: Optional[LogColor] = LogColor.RED):
        if color:
            self._colored_print(message, color, "ERROR")
        else:
            self.logger.error(f"{self.name}: {message}")
    
    def critical(self, message: str, color: Optional[LogColor] = None):
        if color:
            self._colored_print(message, color, "CRITICAL")
        else:
            self.logger.critical(f"{self.name}: {message}")
    
    def success(self, message: str):
        self._colored_print(message, LogColor.GREEN, "SUCCESS")
    
    def fail(self, message: str):
        self._colored_print(message, LogColor.RED, "FAIL")
    
    def warn(self, message: str):
        self._colored_print(message, LogColor.YELLOW, "WARN")
    
    def highlight(self, message: str):
        self._colored_print(message, LogColor.CYAN, "HIGHLIGHT")