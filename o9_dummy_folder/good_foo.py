import logging
from typing import Optional

import numpy as np
from numpy.core.defchararray import array

class Point:
    """Returns a 3d-Array tuple of coordinates"""
    def __init__(self, a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
    def get_point(self):
        return np.array((self.a, self.b, self.c))

class GoodFoo:
    def __init__(self, a, b):
        self.logger = logging.getLogger("o9_logger")
        self.a = a
        self.b = b

    def point_validity_check(self):
        """ Checks if both inputs are valid Points for calculating the Euclidean Distance"""
        if isinstance(self.a, np.ndarray) and isinstance(self.b, np.ndarray):
            return True
        return False

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
            _difference = self.a - self.b
            return _difference
        except Exception as e:
            self.logger.exception("Error in subtracting two numbers - {}".format(e))
            return None

    def mul(self) -> Optional[int]:
        """ Multiplies two numbers """
        try:
            _product = self.a * self.b
            return _product
        except Exception as e:
            self.logger.exception("Error in subtracting two numbers - {}".format(e))
            return None


    def div(self) -> Optional[float]:
        """ Divides two numbers """
        try:
            _quotient = self.a / self.b
            return _quotient
        except Exception as e:
            self.logger.exception("Error in dividing two numbers - {}".format(e))
            return None

    def get_euclidean_distance(self) -> Optional[float]:
        """ Returns the Euclidean Distance between two points """
        try:
            if self.point_validity_check():
                dist_ = np.linalg.norm(self.a - self.b)
                return dist_
            self.logger.warning("Input Point validity fail. Euclidean distance will not be calculated.")
        except Exception as e:
            self.logger.exception("Error in calculating the euclidean distance - {}".format(e))
            return None
        