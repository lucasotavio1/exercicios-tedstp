n = [0] * 10

x = int(input())

n[0] = x

for i in range (1, 10):
    n[i] = n[i - 1] * 2
for i in range (10):
    print(f'N[{i}] = {n[i]}')