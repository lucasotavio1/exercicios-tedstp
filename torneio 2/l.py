n = int(input())

for _ in range(n):
    a, b, c = map(float, input().split())
    media_pond = (a * 2 + b * 3 + c * 5)/10
    print(f'{media_pond:.1f}')
