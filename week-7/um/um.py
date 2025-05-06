import re

def main():
    print(count(input("Text: ")))


def count(s):
    c = 0
    matches = re.findall(r'\bum(\W|\b)', s, re.IGNORECASE)
    for _ in matches:
        c += 1
    return c

if __name__ == "__main__":
    main()
