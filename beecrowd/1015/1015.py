x1, y1 = map(float, input().split())

x2, y2 = map(float, input().split())

d = (x2 - x1)**2 + (y2 - y1)**2

distancia = d**0.5

print('{:.4f}'.format(distancia))
