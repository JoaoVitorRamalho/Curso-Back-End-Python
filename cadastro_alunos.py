#Nome do aluno: João Vítor Ramalho Gonçalves
alunos = []
def menu():
    print('\n===== MENU PRINCIPAL =====')
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos')
    print('3 - Exibir estatísticas')
    print('4 - Buscar aluno')
    print('5 - Excluir aluno')
    print('0 - Sair')

def cadastrar_aluno():
    aluno = {}
    print('Cadastro do aluno(a)')
    aluno['nome'] = input('Digite o nome: ').strip()
    while True: 
        try:
            aluno['idade'] = int(input('Digite a idade: '))
            if aluno['idade'] < 0:
                print('A idade deve ser um número positivo')
                continue
            break
        except ValueError:
            print('Erro, por favor digite um número inteiro no campo idade!')
        
    aluno['curso'] = input('Digite o curso: ').strip()
    notas = []
    for c in range(3):
        while True:
            try: 
                nota = float(input(f'Digite a nota {c+1}: '))
                if nota < 0:
                    print('A nota tem que ser um valor positivo!')
                    continue
                notas.append(nota)
                break
            except ValueError:
                print('Erro, por favor digite um número no campo nota!')
    aluno['notas'] = notas
    aluno['media'] = round(sum(aluno['notas']) / len(aluno['notas']),2) 
    print(f'Cadastro do aluno(a) {aluno["nome"]} confirmado!')
    return aluno

def listar_alunos():
    if len(alunos) > 0:
        for i,aluno in enumerate(alunos):
            print(f'{i+1}. {aluno["nome"]} - {aluno["idade"]} anos - Curso: {aluno["curso"]} - Média: {aluno["media"]}')
    else:
        print('Nenhum aluno cadastrado.')

def exibir_estatisticas():
    menorMedia = min(aluno['media'] for aluno in alunos)
    maiorMedia = max(aluno['media'] for aluno in alunos)
    mediaTurma = sum(aluno['media'] for aluno in alunos) / len(alunos)
    print(f'Total de alunos: {len(alunos)}')
    print(f'Média geral da turma: {mediaTurma:.2f}')
    print(f'Melhor média: {maiorMedia}')
    print(f'Pior média: {menorMedia}')

def buscar_aluno(nome):
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            for c, i in aluno.items():
                print(f'{c}: {i}')
            break
    else:
        print('Aluno não encontrado')               

def excluir_aluno(nome):
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            alunos.remove(aluno)
            print(f'Aluno(a) {nome} removido com sucesso!')
            break
    else:
        print(f'O aluno(a) {nome} não está na lista!')

while True:
    menu()
    try: 
        op = int(input('Escolha uma opção: '))
        match op:
            case 1:
                alunos.append(cadastrar_aluno())
            case 2:
                listar_alunos()
            case 3:
                exibir_estatisticas()
            case 4:
                alunoBuscar = input('Digite o nome do aluno que você quer buscar: ').strip()
                buscar_aluno(alunoBuscar)
            case 5:
                alunoExcluir = input('Digite o nome do aluno que você quer excluir: ').strip()
                excluir_aluno(alunoExcluir)
            case 0:
                print('Saindo do sistema... Até logo!')
                break
            case _:
                print('Opção inválida! Digite novamente')
    except ValueError:
            print('Erro, por favor digite um número inteiro no campo opção!')

#Nome do aluno: João Vítor Ramalho Gonçalves