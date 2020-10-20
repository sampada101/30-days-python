class Circle:
    def __init__(self, radius):
        self.radius = int(radius)

    def getCircumference(self):
        return 2*(22/7)*self.radius

    def getArea(self):
        return (22/7)*(self.radius*self.radius)


radius = input('Radius of the circle: ')
circle = Circle(radius)
print(f'The Circumference of the circle is: {circle.getCircumference()}')
print(f'The area of the cirlce is: {circle.getArea()}')
