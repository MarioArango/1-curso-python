import random

random_number = random.randint(1, 10)
print(random_number)

colors = ['rojo', 'azul', 'verde']
random_color = random.choice(colors)
print(random_color)

cards = ['As', 'Rey', 'Reyna', 'Jota', '10']
random.shuffle(cards)
print(cards)