a = (0, 1, 2, 0)
b = [0, 1, 2, 1]

b[0] = 1
print(b)
# a[0] = 1 não funciona, tupla é imutável
print(a)
print(min(a), min(b))
print(max(a), max(b))
print(a.count(0)) # o numero 0 tem duas ocorrências na tupla a