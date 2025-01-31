import numpy as np  

array1 = np.random.randint(0,101,20)
array2 = np.random.randint(0,101,20)
array3 = np.random.randint(0,101,20)

array_20 = np.arange(0,20)

array1_pares = [(i,num) for i, num in enumerate(array1) if num % 2 == 0]
array2_pares = [(i,num) for i, num in enumerate(array2) if num % 2 == 0]
array3_pares = [(i,num) for i , num in enumerate(array3) if num % 2 == 0]


plot.bar(array_20, array1)
plot.bar(array_20, array2)
plot.bar(array_20, array3)