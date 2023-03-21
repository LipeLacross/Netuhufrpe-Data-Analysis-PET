import pandas as pd
from scipy import stats

# Read data from CSV file
data = pd.read_csv('vacinados-2022.csv', sep=';',
                    on_bad_lines='skip', low_memory=False)

data.dropna(subset=['idade'], inplace=True)#Remove todas as linhas do DataFrame 'data' que contêm valores faltantes (NaN) na coluna 'idade', usando o método dropna() do Pandas. O parâmetro subset=['idade'] é usado para especificar que apenas a coluna 'idade' deve ser verificada para valores faltantes. O parâmetro inplace=True é usado para modificar o DataFrame original, em vez de criar uma cópia.

# Split the data into two samples
# sample1 = data[data['sexo'] == 'FEMININO']['idade']
# sample2 = data[data['sexo'] == 'MASCULINO']['idade']
sample1 = data[data['raca_cor'] == 'PRETA']['idade']
sample2 = data[data['raca_cor'] == 'BRANCA']['idade']


sample1 = pd.to_numeric(sample1, errors='coerce')
#Vai converter as linha para numérico
#O parâmetro errors='coerce' é usado para forçar a conversão dos valores inválidos em NaN 
sample2 = pd.to_numeric(sample2, errors='coerce')


medianaFem = sample1.median()
medianaMasc = sample2.median()
mediaPreto = sample1.mean()
mediaBranco = sample2.mean()

# exibir o resultado
print(mediaPreto)
print(mediaBranco)

# # Perform t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2, equal_var=False)#equal_var pra dizer que eles não tem a mesma quantidade de amostra
#Por fim, você aplicou o teste t de Student às idades dos vacinados em 2021 e 2022 e obteve uma estatística t e um valor p. A interpretação do resultado depende do valor p. Se o valor p for menor que um nível de significância pré-determinado (geralmente 0,05), podemos rejeitar a hipótese nula de que as médias das duas amostras são iguais e concluir que há uma diferença significativa entre as médias das idades dos vacinados em 2021 e 2022.

# # Print results
print("t-statistic:", t_stat)
print("p-value:", p_value)
# Para esse teste ter dado errado com essas samples, o "p-value" tem ser maior que 0.05
# se o p-value passar 0.05 os valores serão estatisticamente iguais

# Interpret results
alpha = 0.05
if p_value > alpha:
    print("Fail to reject the null hypothesis")
else:
    print("Reject the null hypothesis")
