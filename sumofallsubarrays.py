A =[2,1,3]
n = len(A)
ans =0
for i in range(n):
    ans = ans + (n-i)*(i+1)*A[i]
print(ans)

#approach 2

total_sum =0
curr_sum =0
n = len(A)
for i in range(n):
    curr_ele = (i+1) * A[i]
    total_sum +=curr_sum + curr_ele
    curr_sum+= curr_ele
print(total_sum)
