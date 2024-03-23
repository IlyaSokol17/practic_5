kn = int(input('Введите количество кнатов: '))
sk = kn // 29
kn = kn - (29 * sk)
gl = sk // 17
sk = sk - (17 * gl)
if gl != 0:
    print(f'{gl} галлеонов')
if sk != 0:
    print(f'{sk} сиклей')
if kn != 0:
    print(f'{kn} кнатов')
