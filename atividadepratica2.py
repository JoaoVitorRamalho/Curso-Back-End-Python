print('Atividade 1')
contador = 0
print('O valor do contador é ',contador)
contador +=1
print(f'O novo valor do contador é {contador}')
contador -=1
print(f'O novo valor do contador é {contador}')
print('Atividade 2')
PRECO_UNITARIO = 2.5
quantidade = int(input('Digite a quantidade: '))
print(f'O valor total é: {PRECO_UNITARIO*quantidade} R$')
print('Atividade 3')
A = 10
B = 20
A,B = B, A
print(f'O novo valor de A é {A} e o novo valor de B é {B}')
print('Atividade 4')
nS = input('Digite um número: ')
resultado = int(nS) * 2
print(f'O resultado é {resultado}')
print('Atividade 5')
NUMERO_FLOAT = 15.75
string = ' é um número'
print(f'{str(NUMERO_FLOAT)+string}')
print('Atividade 6')
nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura em metros: '))
print(f'{nome} tem {idade} e {altura:.2f} metros de altura')