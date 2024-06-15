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


def p1_sentence(text: str) -> str:
    new_text: list[str] = []
    for word in text.split():
        new_text.append(pig_latin(word))
    return " ".join(new_text)


def main():
    print(p1_sentence("this is a test translation"))


if __name__ == "__main__":
    main()
