import numpy as np
import matplotlib.pyplot as plt # Importar módulo especifico do matplotlib

array_user = np.linspace(0,5,100)

# array_user -> eixo x
# array_user -> eixo y

plt.plot(array_user,array_user, label = 'linear') # Espeficação eixo x, especificação eixo y, Legenda gráfico
plt.xlabel('Eixo X') # Etiqueta Eixo X
plt.ylabel('Eixo Y') # Etiqueta Eixo Y
plt.title('Gráfico simples') # Titulo do Gráfico
plt.legend()
plt.savefig('exp.png') # Guardar a imagem na mesma pasta do ficheiro Python
plt.show() # Mostra o gráfico no visualizador