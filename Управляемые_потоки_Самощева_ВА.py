# Задание 1
a = (6*6)-1 == 8+1 #False
b = 13-7 != (3*2)+1 #True
c = 3*(2-1) == 4-1 #True
print(a, b, c)

#Задание 2
aa = (6*6)-1 >= 8+1 #True
bb = 13-7 <= (3*2)+1 #True
cc = 3*(2-1)> 4-1 #False
print(aa, bb, cc)

#Задание 3
#NameError, тк "true" написано с маленькой буквы
bool_variable = 'true'
print( type(bool_variable)) #<class 'str'>
#это не логическая переменная, тк переменной было задано значение строки в кавычках.
bool_variable_2 = True
print( type(bool_variable_2)) #<class 'bool'>

#Задание 4
user_name = input("Введите имя ")
Dmitriy_check = "Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!"
greetings = "Добро пожаловать!"
if user_name == "Дмитрий":
    print(Dmitriy_check)
if user_name == "Ангелина":
    print(greetings)

#Задание 5
enter_number = 0
if enter_number < 3:
    print("Попробуйте еще раз. У вас осталось {} попыток.".format(3-enter_number))
if enter_number >= 3:
    print("Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. Для разблокировки обратитесь в службу поддержки.")

#Задание 6
statement_one =(2+2+2 >= 6) and (-1*-1 < 0) #False
statement_two = (4*2 <= 8) and (7-1 == 6) #True
print(statement_one, statement_two)

#Задание 7
user_name = input("Введите имя ")
ARM = input("Введите АРМ ")
if user_name == "Дмитрий" and ARM == "1":
    print("Добро пожаловать!")
if user_name == "Ангелина" and ARM == "2":
    print("Добро пожаловать!")
if user_name == "Василий" and ARM == "3":
    print("Добро пожаловать!")
if user_name == "Екатерина" and ARM == "4":
    print("Добро пожаловать!")
if user_name != "Дмитрий" and ARM !="2" and user_name != "Василий" and  user_name != "Екатерина":
    print("Логин или пароль не верный, попробуйте еще раз")
if user_name != "Дмитрий" and ARM !="3" and  user_name != "Екатерина" and  user_name != "Ангелина":
    print("Логин или пароль не верный, попробуйте еще раз")
if user_name != "Дмитрий" and ARM !="4" and user_name != "Василий" and user_name != "Ангелина":
    print("Логин или пароль не верный, попробуйте еще раз")
if user_name == "Дмитрий" and ARM != "1":
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

#Задание 8
mult1 = (2-1 >3) or (-5*2 == -10) #True
mult2 = (9+5<= 15) or (7 != 4+3) #True
print(mult1, mult2)

#Задание 9
user_name = input("Введите имя ")
ARM = input("Введите АРМ ")
if (user_name == "Дмитрий" and ARM == "1") or (user_name == "Ангелина" and ARM == "2") or (user_name == "Василий" and ARM == "3") or (user_name == "Екатерина" and ARM == "4"):
    print("Добро пожаловать!")
else:
    print("Логин или пароль не верный, попробуйте еще раз")
if user_name == "Дмитрий" and ARM != "1":
    print("Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!")

#Задание 10
grade = 0.0
if grade >= 4.0:
    print("A")
elif grade >= 3.0:
    print("B")
elif grade >= 2.0:
    print("C")
elif grade >= 1.0:
    print("D")
else:
    print('F')
