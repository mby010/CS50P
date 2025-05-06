while True:
    try:
        fraction = input('Fraction: ')
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            continue
        fuel = round(x * 100 / y)
        break
    except (ValueError, ZeroDivisionError):
        pass

if fuel >= 99:
    print('F')
elif fuel <= 1:
    print('E')
else:
    print(f'{fuel}%')
