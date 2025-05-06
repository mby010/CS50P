import sys

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].endswith('.py') == False:
    sys.exit('Not a python file')
try:
    n = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip().startswith('#') == False and len(line.strip()) != 0:
                n += 1
    print(n)
except FileNotFoundError:
    sys.exit('File does not exist')
