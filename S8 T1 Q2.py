n = int(input())
i = 0
k = 0
r = []
o = []
m = []
def letra_a(n):
    for i in range(n):
        i*=0
        r.append(i)
    return r    
def letra_b(n):
    for k in range(n):
        k += 1
        o.append(k)
    return o
def letra_c(n):
    for u in range(n):
        m.append(int(input()))
    return m

a= letra_a(n)
b= letra_b(n)
c= letra_c(n)
print(a)
print(b)
print(c)
