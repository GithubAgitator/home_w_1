# 2x^2+3x-4=0

# a = 2
# b = 3
# c = -4
# d = b ** 2 - 4*a*c
# print(d)
# x1 = (-b + d**0.5)/(2*a)
# x2 = (-b - d**0.5)/(2*a)
# print(x1, x2)

# year = 2100
# A = 4
# B = 100
# C = 400
# if (year % A == 0
#     and year % B != 0
#     or year % C == 0):
#     print('Високосный')
# else:
#     print('Невисокосный')


# Существует ли такой треугольник
#
# a = 3
# b = 2
# c = 4
# if a + b > c and b + c > a and a + c > b:
#     print("Yes")
#     if a == b == c:
#         print("Ровносторонний")
#     elif a == b or b == c or a ==c:
#         print('ravnobedr')
#     else:
#         print("Разносторонний")
# else:
#     print("Треугольник не существует")


# Циклы
# n = []
# for i in range(10):
#     num = int(input())
#     n.append(num)
#     if num == 0:
#         break
# print(n)
# print(max(n))

number = int(input())
res = 0
while number != 0:
    res = res + (number % 10)
    number = number // 10
print(res)