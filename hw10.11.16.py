# 16. Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая расчитывает сумму чисел, которые соответствую символам,
#  стоящим между двумя заданными.
# Например, в функцию передаются символы x и z.
# Значит надо вычислить сумму кодов символов x,y,z.

first_s, last_s = "x", "z"

def sum_of_unicode(first_s, last_s):
    num_f = ord(first_s)
    num_l = ord(last_s)
    sum = 0
    for i in range(num_f, num_l+1):
        if num_f <= i and i <= num_l:
            sum = sum + i
    return sum

result = sum_of_unicode(first_s,last_s)
print("The sum of symbol codes is: ", result)

# 20. Вывести сумму всех чисел, которые являются степенью 3ки от 0 до 1000000

n = 3
# n = int(input("Input a digit: "))
def sum_num_of_pow(n):
    pow = 0
    sum = 0
    for i in range(0,1000000):
        if i == n**pow:
            pow = pow + 1
            sum = sum + i
        else:
            pow = pow
    return sum
result = sum_num_of_pow(n)
print("The sum of the numbers which are powers of %d is: %d" % (n, result))

# 23. Написать функцию для поиска среднее арифметическое всех элементов списка.

list = [11, 7, 13, 4]
print("The average value of", (list))

def aver_all_elem(list):
    aver_el = list[0]
    for i in range(len(list)):
        ce = list[i]
        if ce < aver_el:
            aver_el=aver_el+ce
    return aver_el / len(list)

res = aver_all_elem(list)
print("is", res)

# 24. Написать функцию для поиска разницы сумм всех четных и всех нечетных чисел списка. Т.е. От суммы четных чисел вычесть сумму нечетных чисел в списке.

lst = [12, 6, 9, 18, 7, 11, 4]

def dif_sum_ev_od(lst):
    even = 0
    odd = 0
    for i in range (len(lst)):
        ce = lst[i]
        if ce % 2 == 0:
            even = even + ce
        else:
            odd = odd + ce
        ce = ce // 10
    diff = even - odd
    return diff

res = dif_sum_ev_od(lst)
print("The difference sums of even and odd is: ", res)
