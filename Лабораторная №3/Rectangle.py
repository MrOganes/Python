import uuid

class Rectangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.__id = str(uuid.uuid4())
        self.__vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]

    def Get_vertices(self):
        return self.__vertices

    def Get_id(self):
        return self.__id

    def is_intersect(self, pentagon):
        pentagon_vertices = pentagon.Get_vertices()
        for i in range(0, len(self.__vertices)):
            x1, y1 = self.__vertices[i][0],self.__vertices[i][1]
            x2, y2 = self.__vertices[(i+1)%len(self.__vertices)][0],self.__vertices[(i+1)%len(self.__vertices)][1]
            for j in range(0, len(pentagon_vertices)):
                x3, y3 = pentagon_vertices[j][0], pentagon_vertices[j][1]
                x4, y4 = pentagon_vertices[(j + 1) % len(pentagon_vertices)][0], pentagon_vertices[(j + 1) % len(pentagon_vertices)][1]
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

    def is_include(self, pentagon):
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