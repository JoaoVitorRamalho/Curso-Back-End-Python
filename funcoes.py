numeros = [1,2,3,4,5]
resultado = sum(numeros)
print(resultado)

resultado = sum(numeros,10)
print(resultado)

print(len(numeros))

n = [3,2,5,4,91,10]
# n.sort()
# print(n)
print(sorted(n))
print(sorted(n,reverse=True))

def mensagem():
    print('AAAAAAAAAAAAA')
mensagem()

def saudacao(nome,idade):
    print(f'Ola {nome} sua idade é {idade}')
saudacao('Joao',22)

def soma(a,b):
    return a+b
print(f'A soma é {soma(4,5)}')

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    if b == 0:
        return
    else:    
        return a/b

def media(*n):
    if len(n) == 0:
        return
    else:
        return sum(n) / len(n)

def quadrado(n):
    if n == 0:
        return 1
    else:
        return n*n
print(quadrado(2))

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
print(fatorial(9))

a = 5
b = 7
print(soma(a,b))
print(subtracao(a,b))
print(multiplicacao(a,b))
print(divisao(a,b))
print(f'{media(9,8,7,6,5):.2f}')

def med(a,b):
    return soma(a,b) / 2
print(med(3,5))

def contador(* num):
    tam = len(num)
    print(f'Foram recebidos os valores {num} e são ao todo {tam} números')

contador(1,3,4,6,7,8,9)

def dados(**kwargs):
    print('Dados digitados:' )
    for c,v in kwargs.items():
        print(f'{c}: {v}')

dados(nome='Ana',idade=23,cidade='SJE')
dados(produto='notebook',preco=2500)

def exibirMenu():
    print('''Menu do IVAN
    0 - Sair
    1 - Somar''')
    op = int(input('Escolha uma opção: '))
    return op
while True:
    opcao = exibirMenu()
    match opcao:
        case 0:
            print('Saindo do programa...')
            break
        case 1:
            a = int(input('A: '))
            b = int(input('B: '))
            print(soma(a,b))

