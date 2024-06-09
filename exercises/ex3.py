from decimal import Decimal


def run_timing():
    lsf_of_run = []
    while True:
        time_for_run = input("Введите время пробега 10 км: ")
        if not time_for_run:
            break
        try:
            lsf_of_run.append(float(time_for_run))
        except ValueError:
            print("Введите числовое значение!")
    print(
        f"Средний показатель {sum(lsf_of_run) / len(lsf_of_run):.1f}, более {len(lsf_of_run)} пробежек"
    )


def float_int_int(float_, before_, after_):
    float_ = str(float_)
    int_part, fract_part = float_.split(".")
    return float(
        f"{int_part[-before_:0 if not before_ else len(int_part)]}.{fract_part[:after_]}"
    )


def sum_decimal():
    strings = ["0.1", "0.2"]
    dec1 = Decimal(strings[0])
    dec2 = Decimal(strings[1])
    return dec1 + dec2


def main():
    # run_timing()
    print(float_int_int(1234.5678, 0, 3))
    print(sum_decimal())


if __name__ == "__main__":
    main()
