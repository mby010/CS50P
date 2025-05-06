import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif sys.argv[1].lower().endswith('.csv') == False:
    sys.exit('Not a CSV file')
try:
    menu = []
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            menu.append(row)
    print(tabulate(menu[1:], menu[0], tablefmt="grid"))
except FileNotFoundError:
    sys.exit('File does not exist')
