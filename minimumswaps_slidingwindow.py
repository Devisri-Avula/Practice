A =[1,12,10,3,14,10,5]
B = 8
n = len(A)
count =0
bad =0
for i in A:
    if i<=B:
        count+=1
for i in range(count):
    if A[i]>B:
        bad+=1
        
ans = bad
i =1
j = count
while j<n:
    if A[i-1]>B:
        bad-=1
    if A[j]>B:
        bad+=1
    if bad<ans:
        ans = bad
    i+=1
    j+=1
print(ans)
