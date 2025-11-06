#1
def soma_pares(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return a+b
    else:
        return 0

a = int(input('A: '))
b = int(input('B: '))
print(soma_pares(a,b))
soma = lambda a, b: a + b if a % 2 == 0 and b % 2 == 0 else 0
print(soma(a,b))

#2
def quadrado(lista):
    novaLista = []
    for n in lista:
        novaLista.append(n**2)
    return novaLista

numeros = [2,3,4]
print(quadrado(numeros))

quadrados = list(map(lambda x: x**2,numeros))
print(quadrados)

#3
def media(notas):
    media = 0
    for c in (notas):
        media += c
    media /= len(notas)
    if media >= 7:
        print('Aprovado')
    elif media >=5:
        print('Em recuperação')
    else:
        print('Reprovado')

def mediaSimples(notas):
    from functools import reduce
    media = reduce(lambda x,y: x+y, notas) / len(notas)
    if media >= 7:
        print('Aprovado')
    elif media >=5:
        print('Em recuperação')
    else:
        print('Reprovado')

notas = [10,7,9]
media(notas)
mediaSimples(notas)

#4
def maiorIdade(idades):
    maiores = []
    for i in idades:
        if i >=18:
            maiores.append(i)
    return maiores

def maiorIdadeSimples(idades):
    maiores = list(filter(lambda x: x >=18, idades))
    return maiores

idades = [10,20,36,54,65,11,15,17,18,99]
print(maiorIdade(idades))
print(maiorIdadeSimples(idades))

#5
def conversao(temperaturas):
    fahren = []
    for celsius in temperaturas:
        fahren.append(celsius * 1.8 + 32)
    return fahren

def conversaoSimples(temperaturas):
    fahren = list(map(lambda x: x * 1.8 + 32, temperaturas))
    return fahren

temperaturas = [0,25,37,-10,100]
print(conversao(temperaturas))
print(conversaoSimples(temperaturas))

#6
def maior(numeros):
    maior = 0
    for n in numeros:
        if n > maior:
            maior = n
    return maior

def maiorSimples(numeros):
    maior = max(numeros)
    return maior

numeros = [5, 12, 3, 9, 21, 7]
print(maior(numeros))
print(maiorSimples(numeros))

#7
try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    print(f'O resultado da divisão é {a/b:.2f}')
except ValueError:
    print('Erro: você não digitou um número inteiro!')
except ZeroDivisionError:
    print('Erro: não é possível dividir por zero!')

#8
while True:
    try:
        n = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('ERRO: por favor digite um número inteiro')

print('Número digitado: ',n)

#9
while True:
    try:
        arquivo = input('Digite o nome do arquivo: ')
        open(arquivo)
        break
    except FileNotFoundError:
        print('Arquivo não encontrado, digite novamente!')
print('ABRIU')

#10
while True:
    try:
        n = int(input('Digite um número: '))
        if n < 0:
            raise ValueError('Não existe raiz de número negativo!')
        raiz = n ** 0.5  
        print(f'A raiz de {n} é {raiz}')
        break
    except Exception as erro:
        print(f'ERRO: {erro}')

#11   
nome = input('Nome: ')
while True:
    try:
        idade = int(input('Idade: '))
        if idade < 0:
            print('Idade não pode ser negativa!')
            continue
        else:
            break
    except ValueError:
        print('ERRO: digite um número inteiro no campo idade!')
while True:
    try:
        nota = int(input('Nota: '))
        if nota < 0 or nota > 10:
            print('Nota fora do intervalo aceitável! Digite novamente')
            continue
        else:
            break
    except ValueError:
        print('ERRO: digite um número inteiro no campo nota!')
print(f'Nome: {nome}\nIdade: {idade}\nNota: {nota}')

#12
try:
    a = int(input('A: '))
    b = int(input('B: '))
    print('A soma é: ',a+b)
except ValueError:
    print('ERRO: por favor digite um número inteiro')
finally:
    print('Operação concluída')

#13
nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
print(nome.title())

#14
frase = input('Digite uma frase: ')
print(f'A letra A apareceu {frase.lower().count('a')} vezes')
palavras = frase.split()
print(f'Foram digitadas {len(palavras)} palavras')

#15
frase = input('Digite uma frase: ')
print(frase)
print(frase[::-1])

#16
palavra1 = input('Primeira palavra: ').lower()
palavra2 = input('Segunda palavra: ').lower()

if palavra1 in palavra2:
    print('Elas são exatamente iguais')
if palavra1 in palavra2[::-1] or palavra1[::-1] in palavra2:
    print('Elas são anagramas')
else:
    print('São palavras diferentes')

#17
frase = input('Digite uma frase: ').title()
if 'Python' in frase:
    print(frase.replace('Python','Linguagem Python'))
else:
    print('A palavra Python não está na frase')

#18
frase = input('Digite uma frase: ').title()
palavras = frase.split()
for c in palavras:
    print(c)
print(f'Foram digitadas {len(palavras)} palavras')