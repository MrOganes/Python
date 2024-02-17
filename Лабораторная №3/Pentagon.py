import uuid

class Pentagon:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5):
        self.__id = str(uuid.uuid4())
        self.__vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]

    def Get_vertices(self):
        return self.__vertices

    def Get_id(self):
        return self.__id

    def is_intersect(self, rectangle):
        rectangle_vertices = rectangle.Get_vertices()
        for i in range(0, len(self.__vertices)):
            x1, y1 = self.__vertices[i][0],self.__vertices[i][1]
            x2, y2 = self.__vertices[(i+1)%len(self.__vertices)][0],self.__vertices[(i+1)%len(self.__vertices)][1]
            for j in range(0, len(rectangle_vertices)):
                x3, y3 = rectangle_vertices[j][0], rectangle_vertices[j][1]
                x4, y4 = rectangle_vertices[(j + 1) % len(rectangle_vertices)][0], rectangle_vertices[(j + 1) % len(rectangle_vertices)][1]
                if(self.__check_segments_intersection(x1,y1, x2, y2, x3, y3, x4, y4)):
                    return True
        return False

    def __check_segments_intersection(self, x1, y1, x2, y2, x3, y3, x4, y4):
        x_projections_intersect = min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2)
        y_projections_intersect = min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)

        if x_projections_intersect and y_projections_intersect:
            return True
        else:
            return False

    def is_include(self, rectangle):
        rectangle_vertices = rectangle.Get_vertices()

        x_min, x_max = min(x for x, y in self.__vertices), max(x for x, y in self.__vertices)
        y_min, y_max = min(y for x, y in self.__vertices), max(y for x, y in self.__vertices)

        for x, y in rectangle_vertices:
            if x < x_min or x > x_max or y < y_min or y > y_max:
                return False

        if self.is_intersect(rectangle):
                return False
        return True