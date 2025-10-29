lista = [1,2,3,4,5]
frutas = ['Banana','Morango','Maçã']
print(frutas)

f1 = frutas[0]
f2 = frutas[2]

print(f1)
print(f2)

frutas.append('Uva')
print(frutas)

frutas.insert (0, 'Abacaxi')
print(frutas)

frutas.remove('Morango')
print(frutas)

del frutas[2]
print(frutas)

numeros = [7, 5, 78, 32, 10]
l2 = numeros[1:4]
print(numeros)
print(l2)
l3 = numeros[:2:-1]
print(l3)

lista1 = [1,2,3]
lista2 = [4,5]
listatotal = lista1 + lista2
print(listatotal)

idades = [15,32,12,88]#O ultimo é o caio

print(len(idades))
print(max(idades))
print(min(idades))
print(sum(idades))


t = 3 * idades
print(t)

if 20 in idades:
    print('está')
else:
    print('não está')

idades.sort()
print(idades)

idades.sort(reverse=True)
print(idades)