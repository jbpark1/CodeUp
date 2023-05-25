n = int(input())
cnt = 0

arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for i in arr:
    mok=n//i
    rest=n%i
        
    n=n-i*mok
    cnt+=mok
        
    if n<10:
        break

print(cnt)