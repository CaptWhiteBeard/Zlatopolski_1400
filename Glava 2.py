# 2.1.	 Составить программу:
# а) вычисления значения функции
# y = 17x2 – 6x + 13 при любом значении x;
# б) вычисления значения функции
# y = 3a2 + 5a – 21 при любом значении а.

def A(x):
    return 17 * (x ** 2) - 6 * x + 13


def B(a):
    return 3 * (a ** 2) + 5 * a - 21


# 2.2.	 Составить программу вычисления значения функции
# (a2 + 10)/sqrt(a2 + 1) при любом значении а

def fun(a):
    return (a ** 2 + 10) / (a ** 2 + 1) ** (1 / 2)


# 2.3.	 Составить программу:
# а) вычисления значения функции
# sqrt((2a + sin|3a|)/3,56) при любом значении а;
# б) вычисления значения функции
# sin((3,2 + sqrt(1 + x))/|5x|) при любом значении х.

import math


def A(a):
    return math.sqrt((2 * a + math.sin(abs(3 * a))) / 3.56)


def B(x):
    return math.sin((3.2 + math.sqrt(1 + x)) / (abs(5 * x)))


# 2.4.	 Дана сторона квадрата. Найти его периметр.

def perim(a):
    return 4 * a


# 2.5.	 Дан радиус окружности. Найти ее диаметр

def diam(rad):
    return rad * 2


# 2.6.	 Считая, что Земля  – идеальная сфера с  радиусом R ≈
# 6350  км, определить расстояние до линии горизонта от точки
# с  заданной высотой над Землей.

def kacat(hight):
    R = 6350
    return ((hight + R) ** 2 + R ** 2) ** (1 / 2)


# 2.7.	 Дана длина ребра куба. Найти объем куба и  площадь его
# боковой поверхности.

def volcub(a):
    return a ** 3


def Sbok(a):
    return a ** 2


# 2.8. Дан радиус окружности. Найти длину окружности и  площадь круга.
import math


def lenokr(r):
    return math.pi * 2 * r


def Skrug(r):
    return math.pi * (r ** 2)


# 2.9.	 Составить программу:
# а) вычисления значения функции
# z = 2x3 – 3,44xy + 2,3x2 – 7,1y + 2
# при любых значениях х и  y;
# б) вычисления значения функции
# x = 3,14(a + b)3 + 2,75b2 – 12,7a – 4,1
# при любых значениях a и b.

def A(x, y):
    return 2 * x ** 3 - 3.44 * x * y + 2.3 * x ** 2 - 7.1 * y + 2


def B(a, b):
    return 3.14 * (a + b) ** 3 + 2.75 * b ** 2 - 12.7 * a - 4.1


# 2.10.	 Даны два целых числа. Найти:
# а) их среднее арифметическое;
# б) их среднее геометрическое.

def SredArifm(a, b):
    return (a + b) / 2


def SredGeom(a, b):
    return (a * b) ** (1 / 2)


# 2.11.	 Известны объем и масса тела. Определить плотность материала этого тела.

def plotnost(v, m):
    return m / v


# 2.12.	 Известны количество жителей в  государстве и  площадь
# его территории. Определить плотность населения в  этом государстве.


def PlotNasel(Sgos, Njit):
    return Njit / Sgos


# 2.13.	 Составить программу решения линейного уравнения
# ax + b = 0 (a ≠ 0).

def linearEq(a, b):
    if a == 0:
        return "Нет решения"
    else:
        return -b / a


# 2.14.	 Даны катеты прямоугольного треугольника. Найти его
# гипотенузу.

def gipot(a, b):
    return (a ** 2 + b ** 2) ** (1 / 2)


# 2.15.	 Найти площадь кольца по заданным внешнему и  внутреннему радиусам.
import math


def Skolc(Rvnesh, Rvnut):
    if Rvnesh < Rvnut:
        Rvnesh, Rvnut = Rvnut, Rvnesh
    return (math.pi * Rvnesh ** 2) - (math.pi * Rvnut ** 2)


# 2.16.	 Даны катеты прямоугольного треугольника. Найти его
# периметр.

def PerPrTr(a, b):
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return a + b + c


# 2.17.	 Даны основания и  высота равнобедренной трапеции.
# Найти ее периметр.

def Perim(O1, O2, h):
    if O1 > O2:
        c = (O1 - O2) / 2
    elif O2 > O1:
        c = (O2 - O1) / 2

    bok = (h ** 2 + c ** 2) ** (1 / 2)

    return bok * 2 + O1 + O2


# 2.18.	 Составить программу вычисления значений функций
# z = (x + (2 + y)/x2)/(y + 1/(x2 + 10)**(1/2))
# q = 7.25*sin(x) - |y|
# при любых значениях х и  y

import math


def z(x, y):
    return (x + (2 + y) / (x ** 2)) / (y + 1 / (x ** 2 + 10) ** (1 / 2))


def q(x, y):
    return 7.25 * math.sin(x) - abs(y)


# 2.19.	 Составить программу расчета значения функций
# x = (2/(a**2 + 25)+b) / (sqrt(b) + (a+b)/2)
# y = (|a| + 2sinb) / 5.5a
# при любых значениях a и b
import math


def X(a, b):
    return (2 / (a ** 2 + 25) + b) / (b ** (1 / 2) + (a + b) / 2)


def Y(a, b):
    return (abs(a) + 2 * math.sin(b)) / (5.5 * a)


# 2.20.	 Составить программу расчета значения функций
# a = sqrt((abs(e - 3/f))**3 +g)
# b = sin(e) + (cos(h))**2
# c = 33g / (ef - 3)
# при любых значениях e, f, g и h.
import math


def A(e, f, g):
    return math.sqrt((abs(e - 3 / f)) ** 3 + g)


def B(e, h):
    return math.sin(e) + (math.cos(h)) ** 2


def C(g, e, f):
    return 33 * g / (e * f - 3)


# 2.21.	 Составить программу расчета значения функций
# a = (e + f/2)/3
# b = |h2 - g|
# c = sqrt((g-h)2 - 3sin(e))
# при любых значениях e, f, g и h.
import math


def A(e, f):
    return (e + f / 2) / 3


def B(h, g):
    return abs(h ** 2 - g)


def C(g, h, e):
    return ((g - h) ** 2 - 3 * math.sin(e)) ** (1 / 2)


# 2.22.	 Даны два числа. Найти среднее арифметическое и  среднее геометрическое их модулей.

def SredArif(a, b):
    return (abs(a) + abs(b)) / 2


def SredGeom(a, b):
    return (abs(a) * abs(b)) ** (1 / 2)


# 2.23.	 Даны стороны прямоугольника. Найти его периметр
# и длину диагонали.

def PerDiag(a, b):
    Perimetr = a * 2 + b * 2
    Diag = (a ** 2 + b ** 2) ** (1 / 2)

    return Perimetr, Diag


# 2.24.	 Даны два числа. Найти их сумму, разность, произведение,
# а также частное от деления первого числа на второе

def MathOps(a, b):
    summ = a + b
    razn = a - b
    proizv = a * b
    chast = a / b

    return summ, razn, proizv, chast


# 2.25.	 Даны длины сторон прямоугольного параллелепипеда.
# Найти его объем и  площадь боковой поверхности.

def VSparal(a, b, c):
    vol = a * b * c
    Sbok1 = a * b
    Sbok2 = b * c
    Sbok3 = a * c

    return vol, Sbok1, Sbok2, Sbok3


# 2.26.	 Даны координаты на плоскости двух точек. Найти расстояние между этими точками.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Дай мне объект класса Точка")

        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** (1 / 2)


# 2.27.	 Даны основания и  высота равнобедренной трапеции.
# Найти периметр трапеции.

"""Смотри задачу 2.17"""

# 2.28.	 Даны основания равнобедренной трапеции и  угол при
# большем основании. Найти площадь трапеции.
import math


def STrap(O1, O2, angle):
    if O1 > O2:
        O1, O2 = O2, O1

    while angle > 360:
        angle -= 360

    angle = angle * math.pi / 180

    return 0.5 * (O2 ** 2 - O1 ** 2) * math.tan(angle)


# 2.29.	 Треугольник задан координатами своих вершин. Найти
# периметр и  площадь треугольника.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Дай мне объект класса Точка")

        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** (1 / 2)


class Triangle:

    def __init__(self, A, B, C):  # A,B,C - это точки;  a,b,c - это стороны
        self.A = A
        self.B = B
        self.C = C

        self.a = Point.calc_dist(self.A, self.B)
        self.b = Point.calc_dist(self.B, self.C)
        self.c = Point.calc_dist(self.A, self.C)

    @property
    def Perim(self):
        return self.a + self.b + self.c

    @property
    def Square(self):  # Площадь по формуле герона
        p = self.Perim / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)


# 2.30.	 Выпуклый четырехугольник задан координатами своих
# вершин. Найти площадь этого четырехугольника как сумму площадей треугольников.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Дай мне объект класса Точка")

        return ((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2) ** (1 / 2)


class Triangle:

    def __init__(self, A, B, C):  # A,B,C - это точки;  a,b,c - это стороны
        self.A = A
        self.B = B
        self.C = C

        self.a = Point.calc_dist(self.A, self.B)
        self.b = Point.calc_dist(self.B, self.C)
        self.c = Point.calc_dist(self.A, self.C)

    @property
    def Perim(self):
        return self.a + self.b + self.c

    @property
    def Square(self):  # Площадь по формуле герона
        p = self.Perim / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)


class Quadrangle:
    def __init__(self, A, B, C, D):  # 4 точки, задающих вершины этого четырёхугольника
        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.a = Point.calc_dist(self.A, self.B)
        self.b = Point.calc_dist(self.B, self.C)
        self.c = Point.calc_dist(self.D, self.C)
        self.d = Point.calc_dist(self.A, self.D)

    @property
    def Square(self):
        A1 = Triangle(self.A, self.B, self.D)
        A2 = Triangle(self.A, self.D, self.C)

        return A1.Square + A2.Square


# 2.31.	 Известна стоимость 1 кг конфет, печенья и яблок. Найти
# стоимость всей покупки, если купили x кг конфет, у  кг печенья
# и  z кг яблок.

x = float(input("Стоимость конфет за 1 кг: "))
y = float(input("Стоимость печенья за 1 кг: "))
z = float(input("Стоимость яблок за 1 кг: "))


def cost(nx, ny, nz):
    return nx * x + ny * y + nz * z


# 2.32.	 Известна стоимость монитора, системного блока, клавиатуры и  мыши.
# Сколько будут стоить 3 компьютера из этих элементов? N компьютеров?

def cost_pc(number):
    monit = 2
    block = 4  # Это типа известная стоимость компонентов
    klava = 3
    mouse = 1
    return (monit + block + klava + mouse) * number  # А это типа расчёт стоимости комплекта


# 2.33.	 Возраст Тани – X лет, а  возраст Мити – Y лет. Найти их
# средний возраст, а также определить, на сколько отличается возраст каждого ребенка от среднего значения.

def averege(Tanya, Mitya):
    av = (int(Tanya) + int(Mitya)) / 2
    print(f'Средний возраст: {av}')
    print(f'Возраст Тани отличается от среднего на {abs(int(Tanya) - av)}')
    print(f'Возраст Мити отличается от среднего на {abs(int(Mitya) - av)}')


# 2.34.	 Два автомобиля едут навстречу друг другу с  постоянными скоростями V1 и V2
# км/ч. Определить, через какое время автомобили встретятся, если расстояние между ними было S км.

def meet_time(V1=60, V2=60, S=100):
    return f'Через {(V1 + V2) / S} ч автомобили встретятся'


# 2.35.	 Два автомобиля едут друг за другом с постоянными скоростями V1 и V2 км/ч (V1 > V2).
# Определить, какое расстояние будет между ними через 30 мин после того, как первый автомобиль
# опередил второй на S км.

def dist_30mins(V1=80, V2=60):
    if V2 >= V1:
        print("V1 должно быть больше V2")
    else:
        return f'через 30 минут между автомобилями будет {(V1 - V2) / 0.5} км'


# 2.36.	 Известно значение температуры по шкале Цельсия. Найти соответствующее значение температуры по шкале:
# а) Фаренгейта;
# б) Кельвина.
# Для пересчета по шкале Фаренгейта необходимо исходное значение температуры умножить на 1,8 и к результату прибавить
# 32, а по шкале Кельвина абсолютное значение нуля соответствует –273,15 градуса по шкале Цельсия.

def temp_converter(Celsium):
    print(f'{(Celsium * 1.8) + 32} по Фаренгейту')
    print(f'{Celsium + 273.15} по Кельвину')


# 2.37.	 У  американского писателя-фантаста Рэя Бредбери есть
# роман «450 градусов по Фаренгейту».
# Разработать программу,которая определяет, какой температуре по шкале Цельсия
# соответствует указанное в  названии значение. (См. предыдущую задачу.)

def temp_conv(Farenheit):
    return f'{(Farenheit - 32) / 1.8} градусов Цельсия'


# 2.38.	 Напишите программу, в которой вычисляется сумма, разность, произведение, частное и среднее арифметическое
# двух целых чисел, введенных с  клавиатуры. Например, при вводе чисел 2 и  7 должен быть получен ответ вида:
# 2+7=9 2-7=-5 2*7=14 2/7=0.2857142857142857 (2+7)/2=4.5

def mathops(a, b):
    print(f'{a} + {b} = {a + b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b}')
    print(f'({a} + {b}) / 2 = {(a + b) / 2}')
