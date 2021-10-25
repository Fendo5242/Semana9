numero=[]
i=0
while i < 5:
    num = int(input("Ingrese un número: "))
    numero.append(num)
    i+=1
invertidos = numero[::-1]
print(numero)
print(invertidos)