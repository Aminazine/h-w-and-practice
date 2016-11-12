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