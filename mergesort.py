A = [9,3,6,5,1,0]

        
def mergesort(A):
    n = len(A)
    ans =[]
    if len(A)==1:
        return A
    mid= n//2
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])
    left_len = len(left)
    right_len =len(right)
    i,j=0,0
    while i<left_len and j<right_len:
        if left[i]<right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1
    while i<left_len:
        ans.append(left[i])
        i+=1
    while j<right_len:
        ans.append(right[j])
        j+=1
    return ans
print(mergesort(A))
        
    

    
