import pickle
'''
# Cria um objeto qualquer
data = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Abre um arquivo para escrita em modo binário
with open('meu_arquivo.pickle', 'wb') as arquivo:
    # Serializa o objeto e salva no arquivo
    pickle.dump(data, arquivo)
'''
# Abre o arquivo para leitura
with open('meu_arquivo.pickle', 'rb') as arquivo:
    # Carrega o objeto serializado do arquivo
    data_carregada = pickle.load(arquivo)
    data = data_carregada
    print(arquivo.read())
#O objeto guardado n precisa ser novamente inserido com dump
# Imprime o objeto carregado
print(data)
