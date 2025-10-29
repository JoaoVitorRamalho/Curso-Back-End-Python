#LISTAS
#1
# vetor = []
# for c in range(1,51):
#     vetor.append(c)
# print(vetor)
#2
# vetor = []
# for c in range(100,0,-1):
#     vetor.append(c)
# print(vetor)
#3
# vetor = []
# for c in range(1,200,2):
#     vetor.append(c)
# print(vetor)
#4
# vetor = []
# for c in range(0,10):
#     vetor.append(int(input('Digite um número: '))/2)
# print(vetor)
#5
# vetor = []
# for c in range(0,10):
#     vetor.append(int(input('Digite um número: '))**2)
# print(vetor)
#6
# apostas = []
# jogo = []
# for c in range(0,3):
#     for r in range(0,6):
#         jogo.append(int(input('Digite um número da mega sena: ')))
#     apostas.append(jogo[:])
# print(apostas)
#7
# apostas = []
# jogo = []
# sorteio = [1,15,17,25,57,75]
# acertos = 0
# for c in range(10):
#     for r in range(6):
#         jogo.append(int(input('Digite um número da mega sena: ')))
#         if jogo[r] in sorteio:
#             acertos += 1
#     apostas.append(jogo[:])
#     match acertos:
#         case 4:
#             print('Quadra')
#         case 5:
#             print('Quina')
#         case 6:
#             print('Sena')
#     jogo.clear()
#     acertos = 0
# print(apostas)
#MATRIZES
#1
# matriz= [[], []]
# for c in range(2):
#     for i in range(2):
#         matriz[c].append(int(input(f'Digite o valor da linha [{c}][{i}]: ')))
# print(matriz)
#2
# matriz = [[],[],[]]
# for c in range(3):
#     for i in range(3):
#         matriz[c].append(int(input(f'Digite o valor da linha [{c}][{i}]: ')))
# for c in range(3):
#     for i in range(3):
#         print(matriz[c][i],end=' ')
#     print('')
#3
# matriz = [[],[],[]]
# for c in range(3):
#     for i in range(3):
#         matriz[c].append(int(input(f'Digite o valor da linha [{c}][{i}]: ')))

# print(matriz)
# for c in range(3):
#     print(sum(matriz[c]))
#4
# matriz = [[],[],[]]
# for c in range(3):
#     for i in range(3):
#         matriz[c].append(int(input(f'Digite o valor da linha [{c}][{i}]: ')))

# print(matriz)
# soma = 0
# for c in range(3):
#     for r in range(3):
#         soma += matriz[r][c]
#     print(f'A soma da linha {c} é {soma}')
#     soma = 0
#5
# matriz = [[],[],[]]
# for c in range(3):
#     for i in range(3):
#         matriz[c].append(int(input(f'Digite o valor da linha [{c}][{i}]: ')))

# print(matriz)
# soma = 0
# for c in range(3):
#     for r in range(3):
#         if c == r:
#             soma += matriz[c][r]
# print(f'A soma da matriz principal é {soma}')
# soma1 = 0
# for c in range(3):
#     for r in range(3):
#         if c + r == 2:
#             soma1 += matriz[c][r]
# print(f'A soma da matriz secundária é {soma1}')
#6
# matriz = [[],[],[]]
# for c in range(3):
#     somaL = somaC = 0 
#     for i in range(3):
#         matriz[c].append(int(input(f'Digite o valor da linha [{c}][{i}]: ')))
# somaL = somaC = somaD = somaDP = 0
# for c in range(3):
#     somaL = somaC = 0  
#     for r in range(3):
#         if c == r:
#             somaDP += matriz[c][r]
#         if c + r == 2:
#             somaD += matriz[c][r]
#         somaL += matriz[c][r]
#         somaC += matriz[r][c] 

# if somaDP == somaD == somaC == somaL:
#     print('É um quadrado perfeito')
# else:
#     print('Não é um quadrado perfeito')
#7
# matriz = [[],[]]
# for c in range (2):
#     for r in range(3):
#         matriz[c].append(input('Digite um nome: '))
# for c in range(2):
#     for i in range(3):
#         print(matriz[c][i],end=' ')
#     print('')
#8
# matriz = [[],[]]
# for c in range(2):
#     for r in range(2):
#         matriz[c].append(int(input('Digite um valor ')))
# print(matriz)
#9
# matriz = [[],[]]
# matriz2 = [[],[]]
# resultado = [[],[]]
# for c in range(2):
#     for r in range(2):
#         matriz[c].append(int(input('Digite um valor ')))
# for c in range(2):
#     for r in range(2):
#         matriz2[c].append(int(input('Digite um valor ')))
# for c in range(2):
#     for r in range(2):
#         resultado[c][r] = matriz[c][r] + matriz2[c][r]

# print(matriz)
# print(matriz2)
# print(resultado)
#10
matriz = [[],[]]
matriz2 = [[],[]]
resultado = [[],[]]
for c in range(2):
    for r in range(2):
        matriz[c].append(int(input('Digite um valor ')))
for c in range(2):
    for r in range(2):
        matriz2[c].append(int(input('Digite um valor ')))
for c in range(2):
    for r in range(2):
        resultado[c][r] = matriz[c][r] * matriz2[c][r]

print(matriz)
print(matriz2)
print(resultado)