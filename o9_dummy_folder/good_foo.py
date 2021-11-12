import logging
from typing import Optional

class GoodFoo:
    def __init__(self, a, b):
        self.logger = logging.getLogger("o9_logger")
        self.a = a
        self.b = b

    def add(self) -> Optional[int]:
        """ Adds two numbers """
        try:
            _sum = self.a + self.b
            return _sum
        except Exception as e:
            self.logger.exception("Error in adding two numbers - {}".format(e))
            return None

    def sub(self) -> Optional[int]:
        """ Subtracts two numbers """
        try:
            return self.a - self.b
        except Exception as e:
            self.logger.exception("Error in subtracting two numbers - {}".format(e))
            return None

    def mul(self) -> Optional[int]:
        """ Multiplies two numbers """
        try:
            return self.a * self.b
        except Exception as e:
            self.logger.exception("Error in subtracting two numbers - {}".format(e))
            return None


    def div(self) -> Optional[float]:
        """ Divides two numbers """
        try:
            return self.a / self.b
        except Exception as e:
            self.logger.exception("Error in dividing two numbers - {}".format(e))
            return None