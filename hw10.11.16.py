import random
# 16. Каждому символу в таблице символов Unicode соответствует число.
# Написать функцию, которая расчитывает сумму чисел, которые соответствую символам,
#  стоящим между двумя заданными.
# Например, в функцию передаются символы x и z. Значит надо вычислить сумму кодов символов x,y,z.

first_s, last_s = "a", "c"

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
    return sum
result = sum_num_of_pow(n)
print("The sum of the numbers which are powers of %d is: %d" % (n, result))

# 23. Написать функцию для поиска среднее арифметическое всех элементов списка.

list = [11, 7, 13, 4]
print("The average value of", (list))

def aver_all_elem(list):
    sum_el = 0
    for i in range(len(list)):
        sum_el = sum_el + list[i]
        return sum_el / len(list)

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
    diff = even - odd
    return diff

res = dif_sum_ev_od(lst)
print("The difference sums of even and odd is: ", res)

# 25. Создайте список на 50 элементов из всех нечётных чисел от 1 до 99, выведите его на экран
# в строку, а затем этот же список выведите на экран тоже в строку, но в случайном порядке
# (например, 99 11 43 19 … 7 91 3 1).

list = [i for i in range (1,100, 2)]
print(list)
random.shuffle(list)
print(list)

# 26. Создайте 2 списка из 5 случайных целых чисел из отрезка [0;5] каждый, выведите списки на
# экран в двух отдельных строках. Посчитайте среднее арифметическое элементов каждого
# списка и сообщите, для какого из списков это значение оказалось больше (либо сообщите,
# что их средние арифметические равны).

list1 = []
list2 = []
def fill_list(list):
    lst = [random.randint(0, 5) for i in range(5)]
    return lst

lst1, lst2 = fill_list(list1), fill_list(list2)
print("List_1: ", lst1)
print("List_2: ", lst2)

def aver(lst):
    sum = 0
    for i in range(len(lst)):
        sum = sum + lst[i]
    avr = sum / len(lst)
    return avr

res1, res2 = aver(lst1), aver(lst2)
# print("Avarage of List_1:", res1)
# print("Avarage of List_2:", res2)
if res1 > res2:
    print('The average of the "List_1" more than the average of the "List_2"')
if res2 > res1:
    print('The average of the "List_2" more than the average of the "List_1"')
if res1 == res2:
    print('Average values of two lists are equal')

# 27. Создайте список из 11 случайных целых чисел из отрезка [-1;1], выведите список на экран в
# строку. Определите какой элемент встречается в списке чаще всего и выведите об этом
# сообщение на экран. Если два каких-то элемента встречаются одинаковое количество раз,
# то не выводить ничего.

def fill_list(list):
    lst = [random.randint(-1, 1) for i in range(11)]
    return lst

lst = fill_list(list)
print(lst)

def most_freq_elem(list):
    elem = lst[0]
    max_freq = 1
    for i in range(len(lst) - 1):
        freq = 1
        for n in range(i + 1, len(lst)):
            if lst[i] == lst[n]:
                freq += 1
        if freq > max_freq:
            max_freq = freq
            elem = lst[i]
    if max_freq > 1:
        return elem

result = most_freq_elem(lst)
print("The number '%d' is the most common" % (result))

# 28. Создать программу, которая запрашивает у пользователя произвольную строку символов.

text = "год-2016"

def conv(text):
    encr = "абвгдо123456-0"
    conv_txt = ''
    for i in range(len(text)):
        if text[i] in encr:
            conv_txt = conv_txt + encr[(encr.index(text[i]) + 5) % len(encr)]
    return conv_txt
res = conv(text)
print(res)

# 29. Создать генератор паролей, который будет генерировать случайные неповторяющиеся пароли по следующим правилам:
# - Пароль состоит из 8 символов
# - В пароле допускаются только латинские большие и маленькие буквы, цифры и символ подчеркивания
# - Пароль обязательно должен содержать Большие и маленькие буквы и цифры

simb_upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simb_low = "_abcdefghijklmnopqrstuvwxyz"
dig_ch = "1234567890"

def rand(simb):
    for i in range(len(simb)):
        rand_simb = random.randrange(0,len(simb))
        return rand_simb

passw = ""
length = 8
for i in range(length):
    ind = random.randrange(len(simb_upp))
    passw = passw + simb_upp[ind]

for i in range(random.randrange(1,3)):
    rand_ind = random.randrange(len(passw) // 2)
    passw = passw[0:rand_ind] + str(rand(dig_ch)) + passw[rand_ind + 1:]

for i in range(random.randrange(1,3)):
    rand_ind = random.randrange(len(passw) // 2, len(passw))
    passw = passw[0:rand_ind] + simb_low[rand_ind] + passw[rand_ind + 1:]

print(passw)
print(len(passw))


