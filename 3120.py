# n = 1260
# cnt = 0

# coinTypes = [500, 100, 50, 10]

# for i in coinTypes:
#     cnt += n // i
#     n %= i

# print(cnt)

# 방법 1
def cal10(n,t):
    if n<=t:
        return n+10
    else:
        return n-10
def cal5(n,t):
    if n<=t:
        return n+5
    else:
        return n-5
def cal1(n,t):
    if n<=t:
        return n+1
    else:
        return n-1

now, target = map(int, input().split())
cnt = 0

#절대값 이용
while True:
    if now==target:
        break
    
    if abs(now-target)>=10:
        now = cal10(now, target)
        cnt+=1
        continue
        
    elif abs(now-target)>=5:
        new1 = cal10(now, target)
        new2 = cal5(now, target)
        
        if abs(target-new1)<abs(target-new2):
            now=new1
        else:
            now=new2
        
        cnt+=1
        continue
    
    else:
        new1 = cal5(now, target)
        new2 = cal1(now, target)
        
        if abs(target-new1)<abs(target-new2):
            cnt+=abs(target-new1)+1
        else:
            cnt+=abs(target-new2)+1
        
        break
        
print(cnt)