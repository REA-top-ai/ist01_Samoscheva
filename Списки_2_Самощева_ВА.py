#Задание 1
list1 = range (2, 20, 2)
list1_len = len(list1)
print(list1_len)
#9

list1 = range (2, 20, 3)
list1_len = len(list1)
print(list1_len)
#6

#Задание 2
employees = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
index4 = employees[4]
print(len(employees), index4)
print(employees[6])

#Задание 3
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(last_element, element5)

#Задание 4
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0: 2]
print(len(beginning))
#2

beginning = suitcase [0: 4]
print(len(beginning))
#4

middle = suitcase [2:4]
print(middle)

#Задание 5
suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[:3]
print(start)

#Задание 6
votes = ['Jake','Jake', 'Jake', 'Jake', 'Jake', 'Jake', 'Jake', 'Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Laurie', 'Laurie', 'Laurie', 'Cassie', 'Cassie', 'Cassie', 'Cassie', 'Cassie' ]
jake_votes = votes.count('Jake')
print(jake_votes)

#Задание 6
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)

#Задание 7
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

#Задание 8
inventory = ['двухспальная кровать', 'двухспальная кровать', 'изголовье', 'двуспальная кровать', 'двуспальная кровать', 'комод', 'комод', 'стол', 'стол', 'тумбочка', 'тумбочка', 'королевский кровать', 'двуспальная кровать', 'две односпальные кровати', 'две односпальные кровати', 'простыни', 'простыни', 'подушка', 'подушка']
inventory_len = len(inventory) + inventory.count('две односпальные кровати')
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('две односпальные кровати')*2
inventory.sort()
print(inventory)
print(inventory_len)
print(first)
print(last)
print(inventory_2_6)
print(first)
print(twin_beds)

