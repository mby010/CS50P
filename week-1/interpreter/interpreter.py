exp = input('Expression: ').strip()
x, y, z= exp.split(' ')
match y:
    case '+':
        print(float(x) + float(z))
    case '-':
        print(float(x) - float(z))
    case '*':
        print(float(x) * float(z))
    case '/':
        print(float(x) / float(z))

