#Preciso fazer 5 análise estatísticas com pandas, e scipy usando o banco de dados de Recife sobre vacinados de 2021 e 2022
#matplotlib opcional
#As colunas são faixa_etaria;idade;sexo;raca_cor;municipio;grupo;categoria;lote;vacina_fabricante;descricao_dose;cnes;sistema_origem;data_vacinacao

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
#As colunas são: ['faixa_etaria']['idade']['sexo']['raca_cor']['municipio']['grupo']['categoria']['lote']['vacina_fabricante']['descricao_dose']['cnes']['sistema_origem']['data_vacinacao']

dataBase1 = pd.read_csv('vacinados-2022.csv', sep=';', on_bad_lines='skip', low_memory=False)
dataBase2 = pd.read_csv('vacinados-2021.csv', sep=';', on_bad_lines='skip', low_memory=False)
#print(data.head)

dado1S = dataBase1[dataBase1['sexo'] == 'MASCULINO']['sexo']
dado2S = dataBase1[dataBase1['sexo'] == 'FEMININO']['sexo']
dado3S = dataBase2[dataBase2['sexo'] == 'MASCULINO']['sexo']
dado4S = dataBase2[dataBase2['sexo'] == 'FEMININO']['sexo']

mans1 = dado1S.value_counts()
womans1 = dado2S.value_counts()

mans2 = dado3S.value_counts()
womans2 = dado4S.value_counts()
print(mans1)
print(womans1)
print(mans2)
print(womans2)
#Mulheres se vacinaram mais que homens em 2022 e 2021, em 2021 houveram mais pessoas vacinadas.

dataBase1.dropna(subset=['idade'], inplace=True)
dataBase2.dropna(subset=['idade'], inplace=True)

idadesA = pd.to_numeric(dataBase1["idade"], errors='coerce')
idadesB = pd.to_numeric(dataBase2["idade"], errors='coerce')

media_idades1 = idadesA.mean()
mediana_idades1 = idadesA.median()
var_idades1 = idadesA.var()
desvio_padrao_idades1 = idadesA.std()
print(f"Média: {media_idades1:.2f}")
print(f"Mediana: {mediana_idades1}")
print(f"Variância: {desvio_padrao_idades1}")
print(f"Desvio padrão: {desvio_padrao_idades1:.2f}")

media_idades2 = idadesB.mean()
mediana_idades2 = idadesB.median()
var_idades1 = idadesB.var()
desvio_padrao_idades2 = idadesB.std()
print(f"Média: {media_idades2:.2f}")
print(f"Mediana: {mediana_idades2}")
print(f"Variância: {desvio_padrao_idades2}")
print(f"Desvio padrão: {desvio_padrao_idades2:.2f}")

print("Estatísticas descritivas da idade dos vacinados em 2021:")
print(dataBase2["idade"].describe())

print("Estatísticas descritivas da idade dos vacinados em 2022:")
print(dataBase1["idade"].describe())

idade_counts1 = dataBase1['idade'].value_counts()
print(idade_counts1)
idade_counts2 = dataBase2['idade'].value_counts()
print(idade_counts2)
#Média da idade das pessoas vacinadas em 2022 é mais baixa, em 2022 as crianças de 10 anos foram as mais vacinadas e em 2021 as pessoas com 39 anos foram as mais vacinadas.


# filtrar apenas valores válidos de idade para resolver valores infinitos
idadesFilterA = idadesA[(idadesA >= 1) & (idadesA <= 100)]
idadesFilterB = idadesB[(idadesB >= 1) & (idadesB <= 100)]

t_stat, p_value = stats.ttest_ind(idadesFilterA, idadesFilterB, equal_var=False)

print("Teste de diferença entre as médias das idades dos vacinados em 2021 e 2022:")
print("t-statistic:", t_stat)
print("p-value:", p_value)
#t-statistic: -322.36074595762693 e p-value: 0.0
#Portanto, podemos rejeitar a hipótese nula de que as médias das idades dos vacinados em 2021 e 2022 são iguais.

print(np.isfinite(idadesFilterA).all())
print(np.isfinite(idadesFilterB).all())
#Se der false quer dizer que há valores infinitos que precisam ser tratados



vacina_counts1 = dataBase1['vacina_fabricante'].value_counts()
print(vacina_counts1)
vacina_counts2 = dataBase2['vacina_fabricante'].value_counts()
print(vacina_counts2)
#A vacina da Pfizer foi a mais usada em 2021 e 2022.

race_counts1 = dataBase1['raca_cor'].value_counts()
print(race_counts1)
race_counts2 = dataBase2['raca_cor'].value_counts()
print(race_counts2) 
#Pessoas de cor Parda foram as mais vacinadas em 2021 e 2022.

