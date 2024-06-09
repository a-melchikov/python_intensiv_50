def hex_output(hex_num="0x50"):
    if hex_num.startswith("0x"):
        hex_num = hex_num[2:]
    res = 0
    for indx, digit in enumerate(reversed(hex_num)):
        res += (int(digit) if digit.isdigit() else ord(digit.lower()) - 87) * 16**indx
    return res


def triangle_name(name):
    cur_length = 1
    cur_letter = 0
    for x in name:
        cur_letter += 1
        print(x, end=" ")
        if cur_letter == cur_length:
            cur_length += 2
            cur_letter = 0
            print()
    print()


def main():
    print(hex_output())
    triangle_name('fajklkljfasdfdfsdfsd')


if __name__ == "__main__":
    main()
