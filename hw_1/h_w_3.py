number = int(input())
A = 5
B = 10
C = 15
D = 30
if (number % A == 0 and number % B == 0 or number % C == 0) and number % D != 0:
    print("Yes")
else:
    print("no")