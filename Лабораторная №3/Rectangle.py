import uuid
from typing import Tuple, Union
import Pentagon

class Rectangle:
    def __init__(self, x1: Union[int, float], y1: Union[int, float], x2: Union[int, float], y2: Union[int, float], x3: Union[int, float], y3: Union[int, float], x4: Union[int, float], y4: Union[int, float]):
        if not all(isinstance(coord, (int, float)) for coord in [x1, y1, x2, y2, x3, y3, x4, y4]):
            raise TypeError("Координаты вершин должны быть числами")

        vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        if len(set(vertices)) < 4:
            raise ValueError("Вершины прямоугольника не должны совпадать")

        self.__id = str(uuid.uuid4())
        self.__vertices = vertices

    def Get_vertices(self) -> Tuple[Tuple[float, float], ...]:
        return tuple(self.__vertices)

    def Get_id(self) -> str:
        return self.__id

    def is_intersect(self, pentagon) -> bool:
        if not isinstance(pentagon, Pentagon.Pentagon):
            raise TypeError("Переданный объект не является пятиугольником")

        pentagon_vertices = pentagon.Get_vertices()
        for i in range(len(self.__vertices)):
            x1, y1 = self.__vertices[i]
            x2, y2 = self.__vertices[(i + 1) % len(self.__vertices)]
            for j in range(len(pentagon_vertices)):
                x3, y3 = pentagon_vertices[j]
                x4, y4 = pentagon_vertices[(j + 1) % len(pentagon_vertices)]
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

    def is_include(self, pentagon) -> bool:
        if not isinstance(pentagon, Pentagon.Pentagon):
            raise TypeError("Переданный объект не является пятиугольником")

        pentagon_vertices = pentagon.Get_vertices()
        rectangle_vertices = self.__vertices

        x_min = min(v[0] for v in rectangle_vertices)
        x_max = max(v[0] for v in rectangle_vertices)
        y_min = min(v[1] for v in rectangle_vertices)
        y_max = max(v[1] for v in rectangle_vertices)

        for x, y in pentagon_vertices:
            if x < x_min or x > x_max or y < y_min or y > y_max:
                return False
        return True