from Rectangle import Rectangle
from Pentagon import Pentagon

#rectangle и pentagon не пересекаются
rectangle = Rectangle(0, 0, 1, 0, 2, 1, 0, 1)
pentagon = Pentagon(5, 5, 6, 6, 7, 7, 8, 8, 9, 9)
print(rectangle.is_intersect(pentagon), pentagon.is_intersect(rectangle))

#rectangle и pentagon пересекаются
rectangle = Rectangle(0, 0, 2, 0, 2, 1, 0, 1)
pentagon = Pentagon(1, 1, 3, 0, 4, 2, 2, 3, 0.5, 2)
print(rectangle.is_intersect(pentagon), pentagon.is_intersect(rectangle))

#rectangle описывает pentagon
rectangle = Rectangle(0, 0, 4, 0, 4, 3, 0, 3)
pentagon = Pentagon(1, 1, 2, 1, 2, 2, 1.5, 2.5, 1, 2)
print(rectangle.is_include(pentagon), pentagon.is_include(rectangle))

#rectangle и pentagon не описывают дргу друга
rectangle = Rectangle(0, 0, 4, 0, 4, 3, 0, 3)
pentagon = Pentagon(1, 1, 2, 1, 2, 2, 1.5, 2.5, 1, 8)
print(rectangle.is_include(pentagon), pentagon.is_include(rectangle))

#pentagon описывает rectangle
pentagon = Pentagon(-3, 2, 3, 2, 3, -2, -3, -2, -5, 0)
rectangle = Rectangle(-1, 1, 1, 1, 1, -1, -1, -1)
print(rectangle.is_include(pentagon), pentagon.is_include(rectangle))