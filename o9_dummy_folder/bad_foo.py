import numpy as np

class Point:
    def __init__(self, a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
    def get_point(self):
        return np.array((self.a, self.b, self.c))

class BadFoo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def dist(self, p1, p2):
        dist_ = np.linalg.norm(p1 - p2)
        return dist_

    
