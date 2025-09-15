a, b, c = map(float, input().split())

PI = 3.14159

area_tri = a * c/2

area_cir = PI * c ** 2

area_trap = (a + b) * c/2

area_qua = b ** 2

area_ret = a * b

print('TRIANGULO: {:.3f}'.format(area_tri))
print('CIRCULO: {:.3f}'.format(area_cir))
print('TRAPEZIO: {:.3f}'.format(area_trap))
print('QUADRADO: {:.3f}'.format(area_qua))
print('RETANGULO: {:.3f}'.format(area_ret))