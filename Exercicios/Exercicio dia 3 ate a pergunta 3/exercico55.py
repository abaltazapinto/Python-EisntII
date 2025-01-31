import numpy as np 
import matplotlib.pyplot as plt 

# Funcao para encontrar pares e seus indices
def encontrar_pares(array):
    return [(i,num) for i, num in enumerate(array) if num % 2 == 0]

# Criar 3 arrays aleatórios
arrays = [np.random.randint(0,101,20) for _ in range(3)]

# Encontrar pares para cada array
pares_todos = [encontrar_pares(array) for array in arrays]

# Extrair indices e valores
indices, valores = zip(*[item for sublist in pares_todos for item in sublist])

plt.plot(indices, valores, 'o-', label='Valores Pares')
plt.xlabel('Indices')
plt.ylabel('Valores')
plt.title('Grafico de Valores Pares')
plt.legend()
plt.show()
