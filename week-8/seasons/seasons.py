from datetime import date
import re
import sys
import inflect
p = inflect.engine()

def main():
    dob = input('Date of birth: ')
    birth_date = get_date(dob)
    delta = date.today() - birth_date
    delta_minutes = delta.days * 24 * 60
    print(f'{p.number_to_words(delta_minutes, andword="").capitalize()} minutes')


def get_date(d):
    if matches := re.search(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', d):
        return date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))
    sys.exit('Invalid date')


if __name__ == "__main__":
    main()
