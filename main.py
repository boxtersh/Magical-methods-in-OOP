# - - - - - - - - - - - - - -  class Point  - - - - - - - - - - - - - -

class Point:

    def __init__(
            self,
            x ,
            y
    ):

        self.x = x
        self.y = y
        self.start = None
        self.end = None

    def __str__(self):

        return f'x = {self.x}, y =  {self.y}'

    def __add__(self, other):

        new_x = self.x + other.x
        new_y = self.y + other.y

        new_point = Point(new_x, new_y)

        return new_point

    def __sub__(self, other):

        new_x = self.x - other.x
        new_y = self.y - other.y

        new_point = Point(new_x, new_y)

        return new_point

point_1 = Point(2, 7)
point_2 = Point(3, 4)
print(f'\033[36mpoint_1:\033[0m\n{point_1}\n\033[36mpoint_2:\033[0m\n{point_2}\n')
point_3 = point_1 + point_2
print(f'\033[36mpoint_1 + point_2:\033[0m\n{point_3}\n')
point_3 = point_1 - point_2
print(f'\033[36mpoint_1 - point_2:\033[0m\n{point_3}\n')

# - - - - - - - - - - - - - -  class Vector2D  - - - - - - - - - - - - - -

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

    def __add__(self, other):

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

# - - - - - - - - - - - - - -  class Money  - - - - - - - - - - - - - -

class Money:

    def __init__(
            self,
            dollars,
            cents
    ):
        if abs(cents) >= 100:
            self.dollars =+ cents // 100
            self.cents = cents % 100

        else:
            self.dollars = dollars
            self.cents = cents

    def __str__(self):

        money = f'\033[36mДолларов:\033[0m {self.dollars} \033[36mцентов\033[0m: {self.cents}'

        return money

    def from_dollars_cents_is_cents(self):

        cents = self.dollars * 100 + self.cents

        return cents

    def from_cents_is_dollars_cents(self, cents):

        new_dollars = cents // 100
        new_cents = cents % 100
        money = Money(new_dollars, new_cents)
        return money


    def __add__(self, other):

        new_cents = self.from_dollars_cents_is_cents() + other.from_dollars_cents_is_cents()
        money = self.from_cents_is_dollars_cents(new_cents)

        return money

    def __sub__(self, other):

        new_cents = self.from_dollars_cents_is_cents() - other.from_dollars_cents_is_cents()

        if abs(new_cents) < 100:
            money = Money(0, new_cents)

        else:
            money = self.from_cents_is_dollars_cents(new_cents)


        return money


money_1 = Money(5,75)
money_2 = Money(1,351)
print(f'money_1: {money_1}\nmoney_2: {money_2}')

money_3 = money_1  + money_2
print(f'money_1  + money_2 = {money_3}')

money_3 = money_2  - money_1
print(f'money_2  - money_1 = {money_3}')

# - - - - - - - - - - - - - -  class Time  - - - - - - - - - - - - - -

class Time:

    def __init__(
            self,
            hour,
            minutes,
            seconds
    ):

        if abs(seconds) >= 60:

            self.hour = hour
            minutes = minutes + seconds // 60
            self.minutes = minutes
            seconds = seconds % 60
            self.seconds = seconds
            print('1**', self.hour,self.minutes,self.seconds)

        if abs(minutes) >= 60:

            self.hour = hour + minutes // 60
            self.minutes = minutes % 60
            self.seconds = seconds
            print('2**', self.hour, self.minutes, self.seconds)

        else:
            self.hour = hour
            self.minutes = minutes
            self.seconds = seconds

    def __str__(self):

        time = f'часов: {self.hour}\nминут: {self.minutes}\nсекунд: {self.seconds}\n'

        return time

    def __len__(self):

        sec = self.hour * 3600 + self.minutes * 60 + self.seconds

        return sec

    def sec_is_time(self, sec):

        hour = sec // 3600
        min = int((sec / 3600 - hour) * 60 // 1)
        sec = int((((sec / 3600 - hour) * 60) - min) * 60 // 1)

        time = Time(hour, min, sec)

        return time



    def __add__(self, other):

        sec = len(self) + len(other)
        time = self.sec_is_time(sec)

        return time



time_1 = Time(1,25,45)
time_2 = Time(1,35,20)
print(f'time_1:\n{time_1}\ntime_2:\n{time_2}\n')

time_3 = time_1 + time_2
print(time_3)

len(time_1)
print(f'Число секунд во времени time_1 = {len(time_1)}')
