#задание 1
contains_a = lambda word: 'a' in word
print(contains_a("Cat story"))

#задание 2
long_string = lambda string: len(string) > 12
print(long_string("My cat's name is Bodhi"))

#Задание 3
end_in_a = lambda symbol: symbol[-1] == 'a'
print(end_in_a("His leg was broken"))

#Задание4
even_or_odd = lambda  num: 'четное' if num%2 == 0 else 'нечетное'
print(even_or_odd(404))

#Задание 5
multiple_of_three = lambda num: 'кратно трем' if num%3 == 0 else 'не кратное'
print(multiple_of_three(315))

#задание 6
rate_movie = lambda rating: 'Мне понравился этот фильм' if rating > 8.5 else 'Этот фильм был не очень хорошим'
print(rate_movie(9.05050505))
