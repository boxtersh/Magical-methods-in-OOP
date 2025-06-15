class Point:

    def __init__(self, x , y):

        self.x = x
        self.y = y
        self.start = None
        self.end = None

    def __str__(self):

        return f'x = {self.x}, y =  {self.y}'

class Vector2D:

    def __init__(
            self,
            start: Point,
            end: Point
    ) -> None:

        self.start = start
        self.end = end

    def __str__(self):
        vector = (f'Координаты вектора:\n\033[36mначало\033[0m {self.start}\n'
                  f'\033[36mконец\033[0m {self.end}\n\n')
        return vector

    def __add__(self, other: "Point"):

        new_start_x = self.start.x + other.start.x
        new_start_y = self.start.y + other.start.y
        new_point_start = Point(new_start_x,new_start_y)

        new_end_x = self.end.x + other.end.x
        new_end_y = self.end.y + other.end.y
        new_point_end = Point(new_end_x, new_end_y)

        new_vector = Vector2D(new_point_start, new_point_end)

        return new_vector

    def __sub__(self, other):
        new_start_x = self.start.x - other.start.x
        new_start_y = self.start.y - other.start.y
        new_point_start = Point(new_start_x, new_start_y)

        new_end_x = self.end.x - other.end.x
        new_end_y = self.end.y - other.end.y
        new_point_end = Point(new_end_x, new_end_y)

        new_vector = Vector2D(new_point_start, new_point_end)

        return new_vector

    def __mul__(self, scalar: int):

        new_end_x = self.end.x * scalar
        new_end_y = self.end.y * scalar
        new_point_end = Point(new_end_x, new_end_y)

        new_vector = Vector2D(self.start, new_point_end)

        return new_vector

    def len_vector(self):

        len_x = self.end.x - self.start.x
        len_y = self.end.y - self.start.y
        len_vector = (len_x ** 2 + len_y ** 2) ** 0.5

        return len_vector








a = Point(1,1)
b = Point(2, 2)
a1 = Point(3,4)
b2 = Point(7, 8)

vec_1 = Vector2D(a, b)
vec_2 = Vector2D(a1, b2)
print(f'vec_1: {vec_1}\nvec_2: {vec_2}')

vec_3 = vec_1 + vec_2
print(f'\033[36mvec_1 + vec_2:\033[0m {vec_3}')

vec_3 = vec_2 - vec_1
print(f'\033[36mvec_2 - vec_1:\033[0m {vec_3}')

vec_3 = vec_2 * 3
print(f'\033[36mvec_2 * 3:\033[0m {vec_3}')

vec_2.len_vector()
print(f'\033[36mДлинна вектора vec_2:\033[0m {round(vec_2.len_vector(), 3)}')

