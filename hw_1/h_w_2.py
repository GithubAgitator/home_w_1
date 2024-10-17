import math



# d = sqrt(x_2 - x_1)^2 + (y_2 - y_1)^2 формула
x1 = float(input("Введите x1 "))
y1 = float(input("Введите y2 "))
x2 = float(input("Введите x2 "))
y2 = float(input("Введите y2 "))

rast = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Расстояние между точками:", rast)