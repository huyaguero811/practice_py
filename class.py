class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


Point().draw()

point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()     #each object is an instance of our point class