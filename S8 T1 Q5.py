lista_a = []
lista_b = []
lista_c = []
for i in range(25):
    lista_a.append(int(input()))
    lista_b.append(int(input()))
lista_c.insert(0, lista_a)
lista_c.insert(1, lista_b)
print(lista_c)
