j = int(input('Write how many ml of water the coffee machine has: '))
k = int(input('Write how many ml of milk the coffee machine has: '))
l = int(input('Write how many grams of coffee beans the coffee machine has: '))
x = int(input('Write how many cups of coffee you will need: '))
w = x * 200
m = x * 50
b = x * 15
p = j // 200
q = k // 50
r = l // 15
z = min(p, q, r)
n = z - x
if z > x:
    print('Yes, I can make that amount of coffee (and even ' + str(n) + ' more than that)')
elif j >= w and k >= m and l >= b:
    print('Yes, I can make that amount of coffee')
else:
    print('No, I can make only ' + str(z) +' cups of coffee')
