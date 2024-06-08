from random import randint
from tabnanny import check
from typing import Literal


class Game:
    def __init__(self, start_number: int, end_number: int) -> None:
        self.start = start_number
        self.end = end_number
        self.random_number: int = randint(start_number, end_number)
        self.messages_end: list[str] = [
            "Слишком большое",
            "Слишком маленькое",
            f"То, что нужно. Было загадано {self.random_number}",
        ]

    @staticmethod
    def _compare_number(num1: int, num2: int) -> Literal[0, 1, 2]:
        return 0 if num1 > num2 else 1 if num1 < num2 else 2

    def _check_number(self, num) -> bool:
        return not isinstance(num, int) or not self.start <= num <= self.end

    def __call__(self, *args, **kwargs) -> None:
        message: str = ""
        print(f"Угадайте число от {self.start} до {self.end}")
        while not message.startswith("То, что нужно"):
            user_number: int = int(input("Введите число: "))
            if self._check_number(user_number):
                print(f"Число должно быть целым от {self.start} до {self.end}")
            else:
                message = self.messages_end[
                    self._compare_number(user_number, self.random_number)
                ]
                print(message)


def main() -> None:
    game = Game(0, 100)
    game()


if __name__ == "__main__":
    main()
