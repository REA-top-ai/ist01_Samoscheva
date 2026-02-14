#Задание1
tortik = ['торт', 1]

#Задание 2
household_chemicals = [['стиральный порошок', 1],['средство для мытья посуды', 1]]

#Задание 3
names=['Ben', 'Holly', 'Ann']
dogs_names= ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

#Задание 4
orders = ['маргаритки', 'васильки']
orders.append('тюльпаны')
orders.append('розы')
print(orders)

#Задание 5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
broken_prices = [5, 3, 4, 5, 4] + [4]
new_orders = list(zip((orders + ['сирень', 'ирис']), broken_prices))
print(new_orders)

#Задание 6
list1=range(9)
list2 = range(8)
print(list(list1), list(list2))

#Задание 7
list1 = range(5,16,3)
list2 = range(0,40,5)
print(list(list1), list(list2))

#Задание 8
first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age= []
age.append(42)
all_ages = [32, 41, 29] + age
ids = list(range(0,4))
name_and_age = list(zip(first_names, all_ages, ids))
print(name_and_age)