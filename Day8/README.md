## Task: Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.
## Approach: Created Class Circle initialized with radius and made two methods to find circumference and area(circumference = 2πr, area = πr2) (where, π= 22/7)
## Solution:
```
class Circle:
    def __init__(self, radius):
        self.radius = int(radius)

    def getCircumference(self):
        return 2*22/7*self.radius

    def getArea(self):
        return 22/7*self.radius*self.radius


radius = input('Radius of the circle: ')
circle = Circle(radius)
print(f'The Circumference of the circle is: {circle.getCircumference()}')
print(f'The area of the cirlce is: {circle.getArea()}')
```
## Author: Sampada Regmi
