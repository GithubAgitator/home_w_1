number = float(input())

res1 = 0
res2 = 0
n1 = int(number)
n = str(number).split('.')[1] # берем число после запятой
n2 = int(n)
while n1 != 0:
    res1 = res1 + (n1 % 10)
    n1 = n1 // 10

while n2 != 0:
    res2 = res2 + (n2 % 10)
    n2 = n2 // 10
print(res1 + res2)

