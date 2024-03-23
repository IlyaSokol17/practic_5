n = int(input('Введите число до 100: '))
d = n % 10
match d:
    case 1:
        print(f'{n} попугай')
    case 2 | 3 | 4:
        print(f'{n} попугая')
    case 6 | 7 | 8 | 9 | 0:
        print(f'{n} попугаев')
    case _:
        print('что-то не так')