   """Отримує додатне число від користувача."""
    while True:
        try:
            value: float = float(input(prompt))
            if value > 0 and value < 1_000_000:
                return value
            else:
                print("Помилка: введіть число більше 0 і менше 1 000 000.")
        except ValueError:
            print("Помилка: потрібно ввести число.")


def get_int(prompt: str) -> int:
    """Отримує додатне ціле число від користувача."""
    while True:
        try:
            value: int = int(input(prompt))
            if value > 0 and value <= MAX_PRODUCTS:
                return value
            else:
                print(f"Помилка: введіть ціле число від 1 до {MAX_PRODUCTS}.")
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")


def main() -> None:
    print("=" * 48)
    print("          РОЗУМНИЙ КОШИК")
    print("   Розрахунок вартості покупки зі знижками")
    print("=" * 48)
