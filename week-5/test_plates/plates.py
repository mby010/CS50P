def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif '.' in s or '!' in s or '?' in s or ' ' in s:
        return False
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    elif s.isalpha() == True:
        return True
    else:
        for c in s:
            if c.isdigit() == True:
                d = s.find(c)
                break
        if s[d] == '0':
            return False
        elif s[d:].isdigit() == True:
            return True
        return False
if __name__ == "__main__":
    main()
