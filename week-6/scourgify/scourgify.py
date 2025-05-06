import csv
import sys

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
try:
    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            for row in reader:
                house = row['house']
                last, fname = row['name'].split(',')
                first = fname.strip()
                writer.writerow({'first': first, 'last': last, 'house': house})

except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')
