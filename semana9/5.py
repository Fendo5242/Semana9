numeros=[]
suma = 0
for i in range(5):
    mi_numero=int(input("Ingrese un número: "))
    numeros.append(mi_numero)
for numero in numeros:
    suma += numero
promedio=suma/len(numeros)
print("La suma es",suma)
print("El promedio es",promedio)
print("El mayor número es:",max(numeros))
print("El menor número es:",min(numeros))
