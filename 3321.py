#1. 토핑 수
n = int(input())

#2. 도우가격, 토핑가격
a, b = map(int, input().split())

#3. 도우칼로리
c = int(input())

#4. 토핑칼로리
d = []
for i in range(n):
    d.append(int(input()))

#5. 토핑칼로리 내림차순 정렬
d.sort(reverse=True)
#print(d)

#6.
result=0
kcal=0  #토핑칼로리
price=0 #토핑가격

#7. 계산: 1달러당 열량 최대인 거 찾기 = 열량/가격
for i in d:
    kcal+=i
    price+=b
    
    cal=(c+kcal)/float(a+price)
    if result>cal:
        break
    else:
        result=cal

print(int(result))