mensalidade = 100
pago = float(input('Digite quanto você pagou: '))
valorTotal = 0
if pago < mensalidade:
    multa = 0
    valorFalta = (mensalidade - pago)
    multa = valorFalta * 0.1
    valorTotal = multa + valorFalta
    print(f'O valor da sua multa foi de {multa} R$ e o valor total a ser pago é de {valorTotal} R$')
elif pago > mensalidade:
    troco = pago - mensalidade
    print(f'Mensalidade paga, seu troco foi {troco} R$')
else:
    print('Obrigado! Pagamento efetuado')
print('Bom treino!')
match pago:
    case 100:
        print('a')
    case _:
        print('n')