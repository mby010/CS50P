def main():
    while True:
        try:
            fraction = input('Fraction: ')
            fuel = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(fuel))

def convert(fraction):
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
        elif y == 0:
            raise ZeroDivisionError
        return round(x * 100 / y)

def gauge(fuel):
    if fuel >= 99:
        return 'F'
    elif fuel <= 1:
        return 'E'
    else:
        return f'{fuel}%'


if __name__ == "__main__":
    main()
