A = "aaaabaaa"
n = len(A)
ans= ""
def findsubstring(A,l,r):
    n = len(A)
    temp = ""
    while l>=0 and r<n and A[l]==A[r]:
        l-=1
        r+=1
    for i in range(l+1,r):
        temp+=A[i]
    return temp
for i in range(n):
    odd_substring = findsubstring(A,i,i)
    even_substring = findsubstring(A,i,i+1)
    if len(odd_substring)>len(ans):
        ans = odd_substring

    if len(even_substring)>len(ans):
        ans = even_substring
print(ans)
                            
                    
