while True:
    try:
        l = int(input())

        vel = list(map(int, input().split()))

        vel_max = max(vel)
        
        if vel_max < 10:
            print(1)
        elif 10 <= vel_max < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break