# 3.1.	 Дано расстояние в сантиметрах. Найти число полных метров в  нем.

def cm_m(cm):
    return f'В {cm} см {cm // 100} полных метров'


# 3.2.	 Дана масса в  килограммах. Найти число полных центнеров в  ней.

def kg_cent(kg):
    return f'В {kg} кг {kg // 100} центнеров'


# 3.3.	 С  некоторого момента прошло 234 дня. Сколько полных
# недель прошло за этот период?

print(f'За этот период прошло {234 // 7} недель')


# 3.4.	 Написать программу, которая решает следующую задачу:
# «N школьников делят k яблок поровну так, чтобы каждому достались только целые яблоки,
# остальные яблоки остаются в  корзинке. Определить, сколько яблок достанется каждому школьнику
# и  сколько яблок останется в корзинке».

def apples(N, k):
    return f'Каждому школьнику достанется {k // N} яблок, а в корзинке останется {k % N}'


# 3.5.	 Дан прямоугольник с  размерами 543×130 мм. Сколько
# квадратов со стороной 130 мм можно отрезать от него?

def otrezh_kvadrat(a=543, b=130, c=130):
    a1 = a // c
    a2 = b // c
    if a < c or b < c:
        return f"Хер ты получишь квадрат со стороной {c}"
    elif a1 >= 1 and a2 >= 1:
        return f'Ты можешь получить {min(a1, a2)} квадратов'


# 3.6.	 В  купейном вагоне имеется 9 купе с  четырьмя местами
# для пассажиров в каждом. Определить номер купе, в котором находится место с  заданным номером
# (нумерация мест сквозная, начинается с 1).

def kupe(mesto):
    if 0 <= mesto <= 36:
        return f'Ваше место находится в {mesto // 4} купе'
    else:
        return 'Твоё место в другом поезде, идиот'


# 3.7.	 В  подъезде № 1 пятиэтажного жилого дома 15 квартир.
# Определить, на каком этаже этого подъезда находится квартира
# с  заданным номером.
import math


def etazh(kvartira):
    if 0 <= kvartira <= 15:
        return f'Ваш этаж - {math.ceil(kvartira / 3)}'
    else:
        return 'Вали с нашей территории'


# 3.8.	 В кинотеатре имеется 20 рядов мест для зрителей, в каждом из которых расположено 15 кресел.
# Билет для зрителей имеет серию АВ и  номер билета, для первого места в  первом ряду
# равного 01643 (далее этот номер увеличивается согласно условному обозначению мест, имеющему вид, показанный в таблице
# ниже):
# 1 2 … 15
# 16 17 … 30
# … … … …
# 286 287 300
# Определить, в  каком ряду находится место, билет на которое
# имеет заданный серийный номер.

n = 20
m = 15
a = [[0] * m for i in range(n)]  # Здесь создаётся пустой массив

k = 1643
for i in range(n):
    for j in range(m):  # Здесь этот массив заполняется номерами билетов
        a[i][j] = k
        k += 1


def row(bilet):
    if 1643 <= bilet < 1943:
        for i in range(n):
            for j in range(m):
                if a[i][j] == bilet:
                    return f'Ваш ряд: {i + 1}'  # Здесь проверяется условие попадание билета в этот зал
    else:
        return f'Вы не в том кинотеатре'


# 3.9.	 С  начала суток прошло n секунд. Определить:
# а) сколько полных часов прошло с  начала суток;
# б) сколько полных минут прошло с начала очередного часа;
# в) сколько полных секунд прошло с начала очередной минуты.

def time(secunds):
    print(f'С начала суток прошло {secunds // 3600} часов')
    print(f'С начала очередного часа прошло {secunds % 3600} минут')
    print(f'С начала очередной минуты прошло {secunds % 3600 % 60} секунд')


# 3.10.	 Дано целое число k (1 ≤ k ≤ 365). Присвоить целочисленной величине n значение 1, 2, ..., 6 или 0
# в  зависимости от того, на какой день недели (понедельник, вторник, ..., субботу или
# воскресенье) приходится k-й день года, в котором 1  января:
# а) понедельник;
# б) вторник;
# в) d-й день недели (если 1 января– понедельник, то d = 1, если
# вторник – d = 2, ..., если воскресенье – d = 7).

nedela = {1: 'понедельник',
          2: 'вторник',
          3: 'среда',
          4: 'четверг',
          5: 'пятница',
          6: 'суббота',
          7: 'воскресенье'}


def den_nedely(k=1, d=1):
    if k not in range(1, 366):
        return 'В году 365 дней, дебил!'
    elif d not in range(1, 8):
        return "В неделе всего 7 дней, придурок!"

    if d == 1:
        if k % 7 == 0:
            return f'Этот день недели - {nedela.get(k % 7 + 7)}'
        else:
            return f'Этот день недели - {nedela.get(k % 7)}'
    elif d != 1:
        if (k + d - 1) % 7 == 0:
            return f'Этот день недели - {nedela.get((k + d - 1) % 7 + 7)}'
        else:
            return f'Этот день недели - {nedela.get((k + d - 1) % 7)}'


# 3.11.	 С начала 1990 года по некоторый день прошло n месяцев
# и 2 дня. Присвоить целочисленной величине x значение 1, 2, ..., 11
# или 12 в зависимости от того, каким месяцем (январем, февралем
# и т.  п.) является месяц этого дня. Например, при n = 3 значение
# х равно 4.

def mesyac(n):
    return n % 12 + 1


#                   Замечание
#                       В задачах 3.12–3.15 условный оператор не использовать.


# 3.12.	 В  подъезде № 1 пятиэтажного жилого дома 20 квартир.
# Определить:
# 1) на каком этаже этого подъезда находится квартира с заданным номером;
# 2) какой по счету является эта квартира, если квартира с  минимальным номером является первой на этаже.
import math

"""
c = []
m, n, k, r = 4, 5, 1, 1  # Объявление переменных

for i in range(m):
    c.append([])
    r += 1
    for j in range(n):
        c[i].append(k)  # Создание массива квартира - порядковый номер
        k += 4  # Типа c[0] - это 1 порядковый номер, т.о. 1,5,9,13,17 кв - первые на своих этажах
    k = r


def kvartira(nomer):
    print(f'Квартира находится на {math.ceil(nomer / 4)} этаже')  # Находим этаж квартиры
    check = 0
    for i in range(m):
        while nomer not in c[i]:  # Находим, какому массиву принадлежит число, возвращаем его
            i += 1
            check = i
    print(f'Эта квартира по счёту {check + 1} на этаже')
"""


# Рещение, представленное выше рабочее, но не подходит под условие "не использовать услнвные операторы"

def kvartira(nomer):
    print(f'Квартира находится на {math.ceil(nomer / 4)} этаже')
    print(f'Квартира по счёту {abs(nomer - (math.ceil(nomer / 4) - 1) * 4)} на этаже')


# 3.13.	 Дана таблица из 10 строк и  5 столбцов. Определить:
# 1) в какой строке находится значение с порядковым номером
# n, если нумерацию вести построчно сверху вниз, а в каждой
# строке – слева направо;
# 2) в  какой строке находится это значение.
import math

c = []
m, n, k = 10, 5, 1

for i in range(m):  # Данный массив не нужен совсем, он создан только для того, чтобы увидеть двумерный массив
    c.append([])
    for j in range(n):
        c[i].append(k)
        k += 1


def koord(chislo):
    print(f'Данное число находится в {math.ceil(chislo / 5)} строке')
    print(f'Данное число находится в {(abs(chislo - (math.ceil(chislo / 5) - 1) * 5))} столбце')


# 3.14.	 В жилом 9-этажном доме имеется 4 подъезда, на каждом
# этаже – 6 квартир. Определить:
# 1) в каком подъезде находится квартира с заданным номером;
# 2) на каком этаже этого подъезда она находится;
# 3) какой по счету на этаже является эта квартира, если квартира с минимальным номером является первой на этаже.

def kv_pod(nomer):
    podezd = math.ceil(nomer / 54)
    etazh = nomer - (podezd - 1) * 54
    print(f'Данная квартира находится в {podezd} подъезде')
    print(f'Данная квартира находится на {math.ceil(etazh / 6)} этаже')
    print(f'Данная квартира по счёту {abs(nomer - (math.ceil(nomer / 6) - 1) * 6)} на этаже')


# 3.15.	 На складе товары находятся в 10-ярусном стеллаже, разбитом на 8 секций.
# В каждой секции на каждом ярусе предусмотрено 15 мест для товаров. Нумерация мест показана на рис. 3.1.
# Склад обслуживается роботом. Определить, в  какой секции и  на
# каком ярусе робот должен взять товар, находящийся на месте
# с  заданным номером.
#
#
#             Секция 1        Секция 2 …         Секция 8
# Ярус 10
# …
# Ярус 2      121 122 …
# Ярус 1      1 2 … 15        16 17 … 30
#
#                         Рис. 3.1
#
# Вариант задачи  – отличается системой нумерации мест (см.
# рис. 3.2).
#
#             Секция 1        Секция 2 … Секция 8
# Ярус 10     10 20 …
# …
# Ярус 2      2 12 …
# Ярус 1      1 11 … 141      151
#
#                         Рис. 3.2

import math


def tovar1(nomer):
    yarus = math.ceil(nomer / 120)
    sekcia = math.ceil((nomer - 120 * (yarus - 1)) / 15)

    print(f'Данный товар находится в секции {sekcia} на ярусе {yarus}')


def tovar2(nomer):
    yarus = nomer - 10 * (math.ceil(nomer / 10) - 1)
    sekcia = math.ceil(nomer / 150)

    print(f'Данный товар находится в секции {sekcia} на ярусе {yarus}')
