def multiplica(x, y):
    resultado = x
    for _ in range(y-1):
        resultado += x
    return resultado

def exponencia(x, y):
    resultado = x
    for _ in range(y-1):
        resultado = multiplica(resultado, x)
    return resultado


x= int(input("Insira o Primeiro valor Positivo para realizar o cálculo:"))
if(x < 0):
    print("Valor Negativo")
while x < 0:
    x= int(input("Insira um valor Positivo!"))



y = int(input("Insira o Segundo valor Positivo para realizar o cálculo:"))
if(y < 0):
    print("Valor Negativo")
while y < 0:
    y= int(input("Insira um valor Positivo!"))

resultado = exponencia(x,y)
print('{} * {} = {}'.format(x, y, resultado))

