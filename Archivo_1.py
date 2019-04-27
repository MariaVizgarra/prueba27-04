#from Prueba import sumar, sumar3nros, sumar4nros
from Prueba import sumarmejor, sumarpares

print('Ingresar numeros')
x = 50
y = 1
print(x+y)
w = True
print(type(x))
x = False
print(type(x))
v = [1, 2, 3]
for i in v:
    print(i)
    if ((i%2)==0):
        print(i)

s = {
    1 : "as",
    5 : "pp",

}

print(s[1], s[5])




if __name__ == '__main__':
    print(sumarmejor(5, 7))
    print(sumarmejor(2, 3, 4))
    print(sumarmejor(2, 3, 4, 5))
    print(sumarmejor(2, 5, 8, 9, 7, 8, 6))
    print(sumarmejor(2, 5, 8, 9, 7, 8, 6))
    print(sumarpares(2, 5, 50, 10, 18, 15, 22))





