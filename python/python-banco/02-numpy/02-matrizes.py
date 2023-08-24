import numpy as np
array_tri = [[1,2,3],[4,5,6],[7,8,9]]
print(array_tri[1][2])

arr = np.array(array_tri)
print(arr)

print(array_tri[2][:])
print(array_tri[2][1:])
print(array_tri[2][:1])

intervalo = np.arange(0,10) # incremento padrão é de 1 em 1. Poderia ser: np.arange(0, 10, 2)
print(intervalo)
inter__ = np.linspace(0, 10, 3) # de 0 a 10 só 3 elementos e o 10 tá incluso
print(inter__)