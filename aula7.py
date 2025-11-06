nums = [1,2,3,4,5,6,7]

quadrados = list(map(lambda x: x**2, nums))
print(quadrados)

nums1 = [1,8,3,10,5]

pares = list(filter(lambda x: x % 2 == 0, nums1))

print(pares)

from functools import reduce

nums2 = [5,6,7,8,9]

soma = reduce(lambda x, y: x+y, nums2)

print(soma)

silabas = ['Phy', 'ton ', 'Iva']

palavra = reduce(lambda x,y: x+y,silabas)

print(palavra)

num3 = [1,2,3,4,5,6,7,8,9,10]
quadradoP = [x for x in num3 if x % 2 == 0 and x > 5]
print(quadradoP)

resultado = [x for x in num3 if x < 3 or x > 10]
print(resultado)

entrada = 'João Vítor Ramalho Gonçalves'
remove = entrada.strip()
print(remove)
divide = entrada.split()
print(divide)
entrada1 = ['Joao','Vitor','Calma']
junta = ' '.join(entrada1)
print(junta)

entrada2 = 'Abacate'
print(entrada2.find('ate'))

frase = 'Curso em Vídeo Python'
print(frase.replace('Python','Android'))
print(frase.title())