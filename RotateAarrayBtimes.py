A =[1,2,3,4]
B = 2
n = len(A)
b = B%n
i =0
m = n
while i<m:
    temp = A[i]
    A[i] = A[m-1]
    A[m-1] = temp
    i+=1
    m-=1
j =0
l= b
while j<l:
    temp = A[j]
    A[j] = A[l-1]
    A[l-1] = temp
    j+=1
    l-=1
while b<n:
    temp = A[b]
    A[b] = A[n-1]
    A[n-1] = temp
    b+=1
    n-=1
print(A)
