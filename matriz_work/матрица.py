from random import *
a = [[1,2,3] ,
     [2,3,4]
     ,[3,4,5]]
print(a[0])
print(a[1])
print(a[2])
print(a[1][1])
k,n=5,3
row = [0]*n
m = [row] * k
print(m[0])
print(m[1])
print(m[2])





m = []
n , k = 5, 3
for i in range(k):
    m.append([0]*n)
for i in range(n):
    for j in range(k):
        m[j][i] = randint(20,80)
for i in range(k):
    print(m[i])

sum=[0,0,0]
for j in range(3):
  for i in range(5):
    sum[j]+=m[j][i]

    
print(sum)
    
    
    
