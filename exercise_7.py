n, k, m = map(int,input('Введите количество n станций, k станцию отправления, m cтанция назначения ').split)
c = ((n + m) - k - 1)
d = (abs(m - k) - 1)
if c < d:
    print(f'Минимальное количество станций: {c}')
else:
    print(f'Минимальное количество станций: {d}')
