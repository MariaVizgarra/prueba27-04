def sumarmejor(*arg):
    acumulador = 0
    for i in arg:
        acumulador = acumulador + i
    return acumulador

def sumarpares(*arg):
    acu = 0
    for i in arg:
        if ((i%2)==0 and i > 10):
            acu = acu + i
    return acu

