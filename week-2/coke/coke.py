amount = 50
while amount > 0:
    print(f'Amount Due: {amount}')
    i = int(input('Insert Coin: '))
    if i not in [5, 10, 25]:
        continue
    amount -= i

if amount == 0:
    print('Change Owed: 0')
else:
    print(f'Change Owed: {-amount}')
