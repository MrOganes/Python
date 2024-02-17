import uuid
from typing import Tuple, Union
import Rectangle

class Pentagon:
    def __init__(self, x1: Union[int, float], y1: Union[int, float], x2: Union[int, float], y2: Union[int, float], x3: Union[int, float], y3: Union[int, float], x4: Union[int, float], y4: Union[int, float], x5: Union[int, float], y5: Union[int, float]):
        if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]):
            raise TypeError("Координаты вершин должны быть числами")

        vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
        if len(set(vertices)) < 5:
            raise ValueError("Вершины пятиугольника не должны совпадать")

        self.__id = str(uuid.uuid4())
        self.__vertices = vertices

    def Get_vertices(self) -> Tuple[Tuple[float, float], ...]:
        return tuple(self.__vertices)

    def Get_id(self) -> str:
        return self.__id

    def is_intersect(self, rectangle) -> bool:
        if not isinstance(rectangle, Rectangle.Rectangle):
            raise TypeError("Переданный объект не является прямоугольником")

        rectangle_vertices = rectangle.Get_vertices()
        for i in range(len(self.__vertices)):
            x1, y1 = self.__vertices[i]
            x2, y2 = self.__vertices[(i + 1) % len(self.__vertices)]
            for j in range(len(rectangle_vertices)):
                x3, y3 = rectangle_vertices[j]
                x4, y4 = rectangle_vertices[(j + 1) % len(rectangle_vertices)]
                if self.__check_segments_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
                    return True
        return False

    def __check_segments_intersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x_projections_intersect = min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2)
        y_projections_intersect = min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)

        if x_projections_intersect and y_projections_intersect:
            return True
        else:
            return False

    def is_include(self, rectangle) -> bool:
        if not isinstance(rectangle, Rectangle.Rectangle):
            raise TypeError("Переданный объект не является прямоугольником")

        rectangle_vertices = rectangle.Get_vertices()
        x_min, x_max = min(x for x, y in self.__vertices), max(x for x, y in self.__vertices)
        y_min, y_max = min(y for x, y in self.__vertices), max(y for x, y in self.__vertices)

        for x, y in rectangle_vertices:
            if x < x_min or x > x_max or y < y_min or y > y_max:
                return False

        if self.is_intersect(rectangle):
            return False
        return True