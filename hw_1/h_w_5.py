number = int(input())

n1 = True # не найден делитель
if number < 0 or number > 100000:
    print('Число должно быть больше 0 и не больше 100 тысяч')
    number = int(input())
if number == 1:
    n1 == False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            n1 = False
            break

if n1:
    print('Prostoe chislo')
else:
    print('Sostavnoe chislo')

