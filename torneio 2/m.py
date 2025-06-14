n = int(input())

in_cont = 0
out_cont = 0

for _ in range (n):
    x = int(input())
    if 10 <= x <= 20:
        in_cont += 1
    else:
        out_cont += 1
        
print(f'{in_cont} in')
print(f'{out_cont} out') 
