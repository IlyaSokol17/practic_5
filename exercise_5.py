w, h = map(int, input('введите вес (в фунтах) и высоту человека (в дюймах) ' ).split())
h = (h*2.54)/100
w = w*0.453592
bmi =w/(h**2)
bmi = round(bmi, 2)
print('Индекс массы тела : ', bmi)
if bmi < 16 :
    print('выраженный дефицит массы тела')
if 16 <= bmi <= 18.49 :
    print('недостаточная масса тела')
if 18.5 <= bmi <= 24.99 :
    print('норма')
if 25 <= bmi <= 29.99 :
    print('избыточная масса тела')
if 30 <= bmi <= 34.99 :
    print('ожирение первой степени')
if 35 <= bmi <= 39.99 :
    print('ожирение второй степени')
if bmi >=40 :
    print('ожирение третьей степени')