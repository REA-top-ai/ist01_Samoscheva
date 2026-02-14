# Задание 1
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)
#37.77777777777778

def c_to_f(c_temp):
    f_temp = c_temp*(9/5) + 32
    return f_temp
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
#32.0

#Задание 2
def get_force(mass, acceleration):
    return mass * acceleration
train_mass = 10
train_acceleration = 100
train_force = get_force(train_mass,train_acceleration)
print(train_force)
print(f'Поезд GE поставляет {train_force} ньютонов силы')
#1000

def get_energy(mass, c=3*10**8):
    return mass*(c**2)
bomb_mass=1
bomb_energy = get_energy(bomb_mass)
print(f'1 кг бомбы составляет {bomb_energy} Джоулей')
#90000000000000000

def get_work(mass, acceleration, spatium):
    force = get_force(mass, acceleration)
    return force * spatium
train_mass = 22680
train_acceleration = 10
train_distance = 100
train_work = get_work(train_mass,train_acceleration,train_distance)
print(f'Поезд выполняет {train_work} Джоулей за {train_distance} метров.')

#Задание 3
##без def
clothes = 'домашняя одежда'
print('У меня большой гардероб')
print(f'Утром лучше всего подходит {clothes}')
print(f'Днем лучше всего подходит {clothes}')
print(f'Вечером лучше всего подходит {clothes}')
print(f'Ночью лучше всего подходит {clothes}')

meal = 'домашняя еда'
print('мои предпочтения в еде')
print(f'на завтрак лучше всего подходит {meal}')
print(f'на обед лучше всего подходит {meal}')
print(f'на ужин лучше всего подходит {meal}')

##c def
clothes = 'домашняя одежда'
print('У меня большой гардероб')
def sentense():
    return 'лучше всего подходит'
print(f'Утром {sentense()} {clothes}')
print(f'Днем {sentense()} {clothes}')
print(f'Вечером {sentense()} {clothes}')
print(f'Ночью {sentense()} {clothes}')

meal = 'домашняя еда'
print('мои предпочтения в еде')
def sentense2():
    return 'лучше всего подходит'
print(f'на завтрак {sentense2()} {meal}')
print(f'на обед {sentense2()} {meal}')
print(f'на ужин {sentense2()} {meal}')

#Задание 4
Dmitriy_check = 'Дмитрий, твое рабочее место находится в другой комнате.Отойди от чужого компьютера и займись работой!'
norm_employee = 'Добро пожаловать'
mistake = 'Логин или пароль не верный, попробуйте еще раз'
def hope_its_not_Dmitriy (user_name, arm):
    if user_name == 'Дмитрий' and arm != 1:
        return print(Dmitriy_check)
    elif (user_name == 'Дмитрий' and arm == 1) or (user_name == "Ангелина" and arm == "2") or (user_name == "Василий" and arm == "3") or (user_name == "Екатерина" and arm == "4") :
        return print(norm_employee)
    else:
        return print(mistake)
check = hope_its_not_Dmitriy(input('Your name: '),input('ARM: '))

#Задание 5
def count_grade(score):
    if score >= 4.0:
        return "A"
    elif score >= 3.0:
        return "B"
    elif score >= 2.0:
        return "C"
    elif score >= 1.0:
        return "D"
    else:
        return 'F'
print(count_grade(2.0))
