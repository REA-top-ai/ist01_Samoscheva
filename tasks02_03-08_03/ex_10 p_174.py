currency = input('Введите валюту: ')
if currency == 'Рубль':
    five_c = int(input('Количество монет номиналом 5 копеек: '))
    ten_c = int(input('Количество монет номиналом 10 копеек: '))
    fifty_c = int(input('Количество монет номиналом 50 копеек: '))
    sum = five_c * 5 + ten_c * 10 + fifty_c * 50
    if sum == 100:
        print('Поздравляю!')
    elif sum > 100:
        print('Сумма больше рубля')
    else:
        print('Сумма меньше рубля')
elif currency == 'Pound':
    five_c = int(input('number of 5 pence coins: '))
    ten_c = int(input('number of 10 pence coins: '))
    fifty_c = int(input('number of 50 pence coins: '))
    sum = five_c * 5 + ten_c * 10 + fifty_c * 50
    if sum == 100:
        print('Congratulations!')
    elif sum > 100:
        print('Amount more than a pound')
    else:
        print('Amount less than a pound')
elif currency == 'Dollar':
    five_c = int(input('number of 5 cents coins: '))
    ten_c = int(input('number of 10 cents coins: '))
    fifty_c = int(input('number of 50 cents coins: '))
    sum = five_c * 5 + ten_c * 10 + fifty_c * 50
    if sum == 100:
        print('Congratulations!')
    elif sum > 100:
        print('Amount more than a dollar')
    else:
        print('Amount less than a dollar')