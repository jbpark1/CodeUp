pasta = []
juice = []
price = 0.0

for i in range(3):
    pasta.append(float(input()))

for i in range(2):
    juice.append(float(input()))

#select 1 pasta, 1 juice (min)
price = (min(pasta)+min(juice))*1.1

print(format(price, ".1f"))