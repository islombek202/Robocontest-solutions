n=int(input())
s=0
for num in range(1,n + 1):
 if num%3==0 or num%5==0 or num%7==0:
   s+=num
print(s)