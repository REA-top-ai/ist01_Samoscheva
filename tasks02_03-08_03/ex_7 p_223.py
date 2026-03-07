days = int(input('Введите количество дней: '))
total_salary = 0

for day in range(1, days+1):
    days_salary =  2**(day - 1)
    total_salary += days_salary
    print('day|', 'salary in a day|', 'total salary|' )
    print(day,'     ', days_salary/100,'           ',  total_salary/100)

