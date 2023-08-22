a = [0, 1, 2, 3, 4, 5, 6]
print(a)
a.append(7)
print(a)
a.remove(7)
print(a)
print(len(a))
a.remove(1)
print(str(a) + " #removeu numero 1")
a.insert(1,1) # insere número 1 na posição 1
print(a)
print(a[0:3]) # intervalo fechado
a.reverse()
print(a)