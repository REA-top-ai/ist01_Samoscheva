square = [
    [4,9,2],
    [3,5,7],
    [8,1,6]
    ]

def lo_shu(magic_square):
    tipo_square = []
    for stroka in magic_square:
        for num in stroka:
            tipo_square.append(num)
    if sorted(tipo_square) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False
    for stroka in magic_square:
        if sum(stroka) != 15:
            return False
    for stolbets in range(3):
        stolbets_sum = magic_square[0][stolbets] + magic_square[1][stolbets] + magic_square[2][stolbets]
        if stolbets_sum != 15:
            return False
    diagonal1 = magic_square[0][0] + magic_square [1][1] + magic_square[2][2]
    diagonal2 = magic_square[0][2] + magic_square[1][1] + magic_square[2][0]
    if diagonal1 != 15 or diagonal2 != 15:
        return False

    return True
print(lo_shu(square))

