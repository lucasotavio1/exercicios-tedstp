v1, v2, v3 = map(int, input().split())

a = [v1, v2, v3]
b = sorted([v1, v2, v3])

for i in b:
    print(f'{i}')
    
print('')

for j in a:
    print(f'{j}')