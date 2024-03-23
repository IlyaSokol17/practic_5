pin = int(input(''))
def number():
    return (pin // 10000 == 0) and (pin // 100) >= 10

def repeat():
    pin1 = str(pin)
    if (pin1[0] != pin1[1] and pin1[0] != pin1[2] and pin1[0] != pin1[3]) and (pin1[1] != pin1[0] and pin1[1] != pin1[2] and pin1[1] != pin1[3]) and (pin1[2] != pin1[0] and pin1[2] != pin1[1] and pin1[2] != pin1[3]) and (pin1[3] != pin1[0] and pin1[3] != pin1[1] and pin1[3] != pin1[2]):
         return True

def year():
    if 1900 <= pin <=2050:
        return False
    else:
        return True


if number() and repeat() and year():
    print('OK')
else:
    print('ERROR')