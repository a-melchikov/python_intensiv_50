from typing import Any


def mysum(*numbers, start: int = 0) -> int:
    output = start
    for num in numbers:
        if isinstance(num, (list, tuple)):
            output += mysum(*num)
        else:
            output += num
    return output


def myavg(*numbers, start_output=0, start_count=0) -> tuple[int, int]:
    output = start_output
    count = start_count
    for num in numbers:
        if isinstance(num, (list, tuple)):
            nested_output, nested_count = myavg(*num)
            output += nested_output
            count += nested_count
        else:
            output += num
            count += 1
    return output, count


def strings_info(strings: list[str]) -> tuple[int, int, int]:
    if not strings:
        return None
    lengths = list(map(len, strings))
    return min(lengths), max(lengths), sum(lengths) / len(lengths)


def sum_obj(lst_obj: list[Any]) -> int:
    sm = 0
    for obj in lst_obj:
        try:
            int_obj = int(float(obj))
        except Exception:
            pass
        else:
            sm += int_obj
    return sm


words_list = ["apple", "banana", "kiwi", "strawberry", "pear"]
print(mysum([[1, 2, 3, [4, 5, 6, 7], [8], [9]], 10, 11], 12, 13, 14))
print(myavg([[1, 2, 3, [4, 5, 6, 7], [8], [9]], 10, 11], 12, 13, 14))
print(strings_info(words_list))
print(sum_obj([1, "1.5", [2, 3, 4], words_list, {123, 12}]))
