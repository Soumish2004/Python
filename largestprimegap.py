import time

lb=int(input())
ub=int(input())
a=time.time()
a1=a2=0

def is_prime(n):
    c=0
    if n%2!=0:
        for i in range(1,int(n**.5)+1,2):
            if n%i==0:
                c+=1
    c+=1
    if (c == 2 and n%2!=1) or n==2:
        return True
    else:
        return False

for i in range(lb,ub+1):
    if is_prime(i):
        a1=i
        break
l=0
for i in range(a1+1 ,ub+1):
    if is_prime(i):
        a2=i
        if a2-a1>l:
            l=a2-a1
        a1=a2
print(l)
print(time.time()-a)