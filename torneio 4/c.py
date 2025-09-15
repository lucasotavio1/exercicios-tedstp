i = 0.0

while i <= 2.0:
    for k in range(1, 4):
        j = i + k
        if i.is_integer() and j.is_integer():
            print(f'I={int(i)} J={int(j)}')
        elif i.is_integer():
            print(f'I={int(i)} J={j:.1f}')
        elif j.is_integer():
            print(f'I={i:.1f} J={int(j)}')
        else:
            print(f'I={i:.1f} J={j:.1f}')
    i = round(i + 0.2, 1)