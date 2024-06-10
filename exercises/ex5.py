from curses.ascii import ispunct


def pig_latin(string: str) -> str:
    punct = ""
    if ispunct(string[-1]):
        punct = string[-1]
        string = string[:-1]

    if string[0].lower() in "aeiou":
        res = f"{string}way"
    else:
        res = f"{string[1:]}{string[0]}ay"

    res = res + punct
    return res


def main():
    print(pig_latin("eat"))
    print(pig_latin("python"))
    print(pig_latin("hello!"))


if __name__ == "__main__":
    main()
