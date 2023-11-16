def fun(n,k):
    if n==1:
        return 0
    return (fun(n-1,k)+k)%n
A = 5
B = 3
res = fun(A,B)
print(res+1)
    
