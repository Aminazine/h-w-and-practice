import math

# 7. Написать функцию, которая преобразует строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"

us_date = '05.17.2016'

def date_us2eu(date):
    m = date[0:3]
    d = date[3:6]
    y = date[6:10]
    res = d + m +y
    return res

eu_date = date_us2eu(us_date)
print("Task #7",eu_date,"\n")

# 8.Написать функцию, которая получает две строки и помещает первую строку в середину второй. Результат помещается в середину первой. Длину строки можно получить с помощью функции len().

s1, s2 = 'AAAAAA', 'BBBBBBBB'

def put1to2(string1, string2):
    lengt_s1 = len(s1)
    lengt_s2 = len(s2)
    mid_s1 = lengt_s1 // 2
    mid_s2 = lengt_s2 // 2
    res1 = s2[0:mid_s2] + s1 + s2[mid_s2:lengt_s2]
    res2 = s1[0:mid_s1] + res1 + s1[mid_s1:lengt_s1]
    return res2

print("Task #8", put1to2(s1, s2))
print()

# 10. Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в консоли, без использования операторов цикла.

num = int(input("Input three-digit number: "))

def sum_of_n(number):
    d1 = number // 100
    d2 = number % 100 // 10
    d3 = number % 10
    ds = d1 + d2 + d3
    return ds

sum = sum_of_n(num)

print("The sum of digits:",sum, "\n")

# 12. Написать функцию, которая будет проверять четность некоторого числа.

num = int(input("Input an integer: "))

if num % 2 == 0:
    print ("An even \n")
else:
    print("Not even \n")

# 13. Написать функцию, которая отвечает на вопрос, пересекаются ли две заданные окружности на плоскости. Каждая окружность задается координатами центра и радиусом.

x1, y1, r1 = 5, 2, 2
x2, y2, r2 = 1, 4, 4

# 1. D = расстояние меж центрами (x1, y1) и (x2, y2); SumR сумма радиусов r1+r2
# Если расстояния между центрами окруж. меньше или равны сумме радиусов этих окружн., то окруж. пересек.
# Расстояние между двумя точками A1(x1;y1) и A2(x2;y2) в прямоугольной системе координат выражается формулой: d=sqrt((x2−x1)^2+(y2−y1)^2)

D = math.sqrt((x2-x1)**2+(y2-y1)**2)

SumR = r1 + r2

if D <= SumR:
    print("Yes. The circles intersect \n")
else:
    print("No. The circles do not intersect \n")

# 14. Два поезда движутся на скорости V1 и V2 навстречу друг другу. Между ними 10 км. пути. Через 4 км пути первый поезд может свернуть на запасной путь. При заданных скоростях узнать столкнутся ли поезда.

V1 = float(input("Input speed of traine #1: "))
V2 = float(input("Input speed of traine #2: "))

H = 10
h1 = 4
h2 = H-h1

time1 = h1/V1
time2 = h2/V2

if time1 < time2:
    print("Trains don't clash \n")
else:
    print("Trains clash \n")

# 15. Написать функцию решения квадратного уравнения.
# ax^2 + bx + c = 0
# a, b и c даны
# Надо найти x
# Дискриминант D = b^2 - 4ac.
# Если D < 0, корней нет, уравнение решений не имеет.
# Если D = 0, корень один.
# Если D > 0, корня два.
# Корни вычисляем по формулам x1 = (-b+√d) / 2a; x2 = (-b-√d) / 2a.

print("Enter the coefficients of the quadratic equation")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c

print("Discriminant = %.2f" % D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print (" x1 = %.2f \n x2 = %.2f" % ( x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Discriminant < 0, equation has no solutions")
