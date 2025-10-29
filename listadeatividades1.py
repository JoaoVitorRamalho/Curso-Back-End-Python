n = int(input('Digite um número: '))
fat = 1
if n < 0:
    print('O fatorial de 0 é 1')
else:
    for c in range (1,n+1):
        fat *=c
print(f'O fatorial de {n} é {fat}')