import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y **2)

    def normalize(self):
        if self.magnitude() == 0:
            m = Vector2D(1e-6, 1e-6)
        m = self.magnitude()
        return Vector2D(self.x / m, self.y / m)

    def __repr__(self):
        return f"<{self.x}, {self.y}>"