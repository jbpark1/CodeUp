# 방법 2
now, target = map(int, input().split())
cnt = 0

# 경우의 수 분류
arr1 = [1,5]        #cnt=1
arr2 = [2,4,6,9]    #cnt=2
arr3 = [3,7,8]      #cnt=3

div = abs(now-target)//10
mdl = abs(now-target)%10

cnt+=div

if mdl in arr1:
    cnt+=1
elif mdl in arr2:
    cnt+=2
elif mdl in arr3:
    cnt+=3

print(cnt)