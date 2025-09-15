leds_por_digito = {
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
    '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}

n = int(input())

for _ in range(n):
    num = input()

    total_leds = sum(leds_por_digito[d] for d in num)
    
    print(f'{total_leds} leds')