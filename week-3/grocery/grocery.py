items =  {}
while True:
    try:
        item = input().upper()
        if item == '':
            break
        elif item in items:
            items[item] += 1
        else:
            items[item] = 1

    except EOFError:
        break

for e in sorted(items):
    print(f'{items[e]} {e}')

