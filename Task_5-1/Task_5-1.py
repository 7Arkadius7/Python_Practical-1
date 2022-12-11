print('Пожалуйста введите координаты точки A:')
xa = float(input('X:'))
ya = float(input('Y:'))
za = float(input('Z:'))
print('Пожалуйста введите координаты точки B:')
xb = float(input('X:'))
yb = float(input('Y:'))
zb = float(input('Z:'))

from math import sqrt
print('Расстояние между точками A и B = ',round(sqrt((xa - xb)**2 + (ya - yb)**2+(za-zb)**2), 2))
