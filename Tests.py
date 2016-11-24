### Test 1 ###
import random
## 1 point #

a, b, c = 12, 9, 16

# 1.  (a+b*c)**2/(c-1)
print(round(((a+b*c)**2)/(c-1),2))

# 2.  a - 4 * b / c
print(round(a-4*b/c, 2))

# 3.  (a * b + 4)
print(round(a*b+4, 2))

## 2 points #

# 4. Найти произведение нечетных цифр пятизначного целого числа.

n = int(input("Input the five-digit number: "))

def multip_of_n(n):
    mult = 1
    for i in range(6):
        if n % 2 == 1:
            mult = mult * (n % 10)
        n = n // 10
    return mult

print (multip_of_n(n))

# 5. Создать программу, выводящую на экран ближайшее к 10 из двух чисел.

x = 10
a = 8.5
b = 11.45
if (x - a) > (x - b):
    print("b")
if (x - a) < (x - b):
    print("a")
if (x - a) == (x - b):
    print("a,b")

# 6. Создать массив из 10 элементов и проинициализировать его простыми числами в случайном порядке

lst = [0]*10
for i in range(2, 100):
   for j in lst:
         if i % j == 0:
             break
   else:
       lst.append(i)
random.shuffle(lst)
print (lst)

## 4 points

# 7. Найти сумму десяти первых чисел ряда Фиббоначчи.

n = 10

def fibon_sum(n):
    fib_sum = 0
    fib1 = 1
    fib2 = 1
    for i in range(1, n):
        fib_sum += fib1
        fib_n = fib1
        fib1 = fib2
        fib2 += fib_n
    return fib_sum

print("The sum of ten Fibonacci numbers is: ",fibon_sum(n))

# 8. В одномерном массиве поменять местами минимальный и максимальный
#    элементы. Остальные оставить на своих местах.

lst = [i for i in range (-7,10)]

print(lst)

min, max = 0, 0
for i in range(len(lst)):
    if lst[i] < lst[min]:
        min = i
    elif lst[i] > lst[max]:
        max = i
print("Min: ", lst[min], "Max: ", lst[max])
n = lst[min]
lst[min] = lst[max]
lst[max] = n

print(lst)

# 9. Нормировать одномерный массив случайных чисел. Нормирвание означает
#    приведение всех значений массива к интервалу [-1;1], причем максимальное
#    абсолютное значение элементов после нормирование должно быть равно 1.
#    Например, последовательность {-5, 3, 4} после нормирование будет выглядеть
#    {-1, 0.6, 0.8}

lst = [i for i in range (-7,6)]

def abs_max(lst):
   return max([abs(x) for x in lst])

abs_num = abs_max(lst)

for i in range (len(lst)):
    i = round(i,2)
    lst[i] = lst[i] / abs_num

r_lst = [round(elem,2) for elem in lst]
print(r_lst)

## 8 points

# 10. Вывести на экран матрицу, транспонированную заданной (3*8)

lst = [[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16],[17,18,19,20,21,22,23,24]]

for elem_list in lst:
   for elem in elem_list:
       print(elem, end="\t")
   print("")

#11. В двумерном массиве отсортировать четные столбцы по возрастанию, а
#    нечетные - по убыванию

arr = [[-9, 14, 5, 6], [7, 19, -3, 11], [14, 5, 2, 7], [5, 10, 19, 0]]

for i in range(len(arr)):
   for j in range(len(arr)):
           num_arr = arr[i][j]
           arr_idx = i
           for n in range(i, len(arr)):
               if j%2 !=0 and num_arr > arr[n][j]:
                   num_arr = arr[n][j]
                   arr_idx = n
               elif j%2 == 0 and num_arr < arr[n][j]:
                   num_arr = arr[n][j]
                   arr_idx = n
           arr[arr_idx][j] = arr[i][j]
           arr[i][j] = num_arr

print("odd","\t","even","\t","odd","\t","even")

for elem_list in arr:
    for elem in elem_list:
        print(elem, end="\t\t ")
    print("")


# 12. Напишите программу, которая будет выводить на экран 15 случайных примеров из таблицы умножения.