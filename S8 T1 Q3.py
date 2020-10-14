posicoes = int(input('posicoes:'))
qtd_notas = int(input('n° notas:'))
letra = int(input('numero de letras: '))
lista_1 = []
lista_2 = []
lista_3 = []
def letra_a(posicoes):
    for i in range(posicoes):
        r = float(input('valores:'))
        r = round(r, 4)
        lista_1.insert(0, r)
    return lista_1
def letra_b(qtd_notas):
    media = 0
    for k in range(qtd_notas):
        nota = float(input('notas:'))      
        lista_2.append(nota)
        media = sum(lista_2)/qtd_notas
        media = round(media, 1)
    return lista_2, media
def letra_c(letra):
    for t in range(letra):
        lista_3.append(input('letras agora: ')[0].lower())
                
a = letra_a(posicoes)
b = letra_b(qtd_notas)
c = letra_c(letra)
print(a)
if qtd_notas==0:
    print('sem notas')
else:
    print(b)
cont =0
for t in lista_3:
    if t in('a','e','i','o','u'):
        cont+=1
    else:
        print(t)
print('numero de vogais',cont)

