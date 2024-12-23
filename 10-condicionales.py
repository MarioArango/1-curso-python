x = 5
if x > 5:
    print('X es mayor que 5')
elif x == 5:
    print('X es igual que 5')
else:
    print('X es menor que 5')

y = 4
if x > y and x > 3:
    print('X es mayor a Y, tambien es mayor a 5')
elif x < y or x < 3:
    print('X es menor que Y que 3')

if (not 5 < 10) or 3 == 3:
    print('5 es menor que 10')