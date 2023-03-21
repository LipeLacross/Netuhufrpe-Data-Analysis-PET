import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt
import random


# notas = [10, 2, 3, 5, 7.5, 3, 5]
# notas = [5, 3, 3, 5, 5, 3, 5]

notas = []
for i in range(100):
    nota = random.randint(0, 10)
    notas.append(nota)

x = np.array(notas)
# mais facilmente, podemos utilizar o metodo numpy.mean
media = np.mean(x)
mediana = np.median(x)
# calcular a variância amostral
variance = np.var(x)
moda = st.mode(x)

print("a média das notas é ", media) 
print("a mediana das notas é ", mediana)
print("a variância das notas é ", variance) #variância vai ser adicionada e subtraída com base na média 
#Se média = 6 e variância = 2, quer dizer que a média vai variar de 8 até 4  
print(f"a moda das notas é {moda}")


# calcular o percentil 25
percentil25 = np.percentile(x, 25) # resultado: 2 #Significa que 25% dos valores da lista estão abaixo de 2 e 75% acima de 2

# calcular o percentil 50 = (mediana)
mediana = np.percentile(x, 50)

# calcular o percentil 75
percentil75 = np.percentile(x, 75)

# exibir os resultados
print(percentil25)
print(mediana)
print(percentil75)

plt.hist(x, bins=10)
plt.title('Histograma')
plt.ylabel('Frequencia')
plt.xlabel('Nota')
plt.show()

fig = plt.figure(figsize=(10, 7)) #tamanho 10 por 7
# Creating plot
plt.boxplot(x)
# show plot
plt.show()
