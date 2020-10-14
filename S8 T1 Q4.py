lista = []
par = []
impar = []
for i in range(20):
    lista.append(int(input()))
for i in lista:
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)
print(par)
print(impar)
