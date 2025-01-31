import numpy as np 

array_aleatorio = np.random.randint(0,101,20)

pares_e_indices = [(i,num) for i, num in enumerate(array_aleatorio) if num % 2 == 0]

print("Array aleatorio:", array_aleatorio)
print("Array e indices: ", pares_e_indices)