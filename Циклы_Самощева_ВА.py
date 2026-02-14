#Задание1
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
for sport in sport_games:
    print(sport)

#Задание 2
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)

#Задание 3
student_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
student_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in student_period_A:
    student_period_B.append(student)
    print(student_period_B)

#Задание 4
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog_breeds in dog_breeds_available_for_adoption:
    print(dog_breeds)
for dog_breeds in dog_breeds_available_for_adoption:
    if dog_breeds == dog_breed_I_want:
        print('У них есть собака, которую я хочу!')
        break

#Задание 5
scoops_sold = 0
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for sales in sales_data:
    for sales01 in sales:
        scoops_sold += sales01
print(scoops_sold)

#Задание 6
single_digits = range(10)
squares = []
for num in single_digits:
    squares.append(num ** 2)
    print(num)
print(squares)
cubes = [digit**3 for digit in single_digits]
print(cubes)

