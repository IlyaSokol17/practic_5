n, m, c = map(int, input('Введите высоты 3-х башен: ').split())
if n <= m <= c:
    print(c, n, m)
if n <= c <= m:
    print(m, c, n)
if m <= n <= c:
    print(c, n, m)
if m <= c <= n:
    print(m, c, m)
if c <= n <= m:
    print(m, n, c)
if c <= m <= n:
    print(n, m, c)