print('Пожалуйста введите координаты точки A:')
xa = float(input('X:'))
ya = float(input('Y:'))
print('Пожалуйста введите координаты точки B:')
xb = float(input('X:'))
yb = float(input('Y:'))

from math import sqrt
print('Расстояние между точками A и B = ',round(sqrt((xa - xb)**2 + (ya - yb)**2), 3))
