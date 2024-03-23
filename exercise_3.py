n = int(input('Введите четырехзначное число :'))
n_1 = n % 10
n = n // 10

n_2 = n % 10
n = n // 10

n_3 = n % 10
n = n // 10

n_4 = n % 10
n = n // 10

n_reversed = n_1 * 1000 + n_2 * 100 + n_3 * 10 + n_4
print(n_reversed)