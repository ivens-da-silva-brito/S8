l=[]
cont=0
while cont<10:
    l.append(int(input()))
    cont +=1
soma= 0 
m =1
for i in l:
        m*=i
        soma+=i
        
print('multiplica', m)
print(l)
print('soma', soma)
