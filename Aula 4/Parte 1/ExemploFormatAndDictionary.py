Inome = "Neto"
frase = f"Frase com variável {Inome}"
print(frase)

# Criando um dicionário para armazenar informações dos alunos
alunos = {
    'João': {'idade': 20, 'curso': 'Engenharia'},
    'Maria': {'idade': 21, 'curso': 'Medicina'},
    'Pedro': {'idade': 19, 'curso': 'Direito'}
}

# Acessando as informações de um aluno específico
print(alunos['João'])   # {'idade': 20, 'curso': 'Engenharia'}
print(alunos['Maria']['curso'])   # 'Medicina'

# Adicionando um novo aluno
alunos['Ana'] = {'idade': 22, 'curso': 'Psicologia'}

# Atualizando as informações de um aluno existente
alunos['Pedro']['curso'] = 'Ciências Econômicas'

# Removendo um aluno
del alunos['Maria']

# Percorrendo o dicionário e imprimindo as informações dos alunos
for Inome, info in alunos.items():
    print(Inome + ':')
    print('   Idade:', info['idade'])
    print('   Curso:', info['curso'])

