# Програма "Розумний кошик" — розрахунок вартості покупки зі знижками

# Константи програми
DISCOUNT_LIMIT: float = 1700.0
DISCOUNT_RATE: float = 0.10
VIP_DISCOUNT_RATE: float = 0.05
MAX_PRODUCTS: int = 20
CURRENCY: str = "грн"


def get_float(prompt: str) -> float:
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

    # Введення текстової інформації
    customer_name: str = str(input("Введіть ім'я покупця: ")).strip()
    if not customer_name:
        customer_name = "Покупець"

    # Кількість різних товарів у замовленні
    product_count: int = get_int("Скільки різних товарів бажаєте придбати? ")

    total: float = 0.0
    receipt: list[tuple[str, float, int, float]] = []

    # Введення даних про кожен товар та обчислення вартості
    for number in range(1, product_count + 1):
        print(f"\nТовар №{number}")
        product_name: str = str(input("Назва товару: ")).strip()
        if not product_name:
            product_name = f"Товар №{number}"

        price: float = get_float("Ціна за одиницю (грн): ")
        quantity: int = get_int("Кількість одиниць: ")

        item_total: float = price * quantity
        total += item_total
        receipt.append((product_name, price, quantity, item_total))

    # Логічна змінна bool визначає право на знижку
    has_discount: bool = bool(total >= DISCOUNT_LIMIT)

    # Вкладені умови: перевірка знижки та статусу покупця
    is_vip: bool = input("\nПокупець має VIP-картку? (так/ні): ").strip().lower() == "так"

    discount_rate: float = 0.0
    if has_discount:
        discount_rate = DISCOUNT_RATE
        if is_vip:
            discount_rate += VIP_DISCOUNT_RATE
    elif is_vip:
        discount_rate = VIP_DISCOUNT_RATE
    else:
        discount_rate = 0.0

    discount: float = total * discount_rate
    final_total: float = total - discount

    # Умовний вираз для визначення категорії покупки
    purchase_category: str = (
        "велика покупка" if total >= DISCOUNT_LIMIT
        else "звичайна покупка"
    )

    # Вибір способу оплати за допомогою match-case (Python 3.10+)
    print("\nСпосіб оплати:")
    print("1 — Готівка")
    print("2 — Банківська картка")
    print("3 — Онлайн-оплата")

    payment_choice: str = input("Ваш вибір (1/2/3): ").strip()

    match payment_choice:
        case "1":
            payment_method: str = "Готівка"
        case "2":
            payment_method = "Банківська картка"
        case "3":
            payment_method = "Онлайн-оплата"
        case _:
            payment_method = "Не вибрано (оплата уточнюється)"

    # Додаткова перевірка логічними операторами and, or, not
    if (discount_rate > 0 and final_total < total) or not customer_name:
        discount_message: str = "Знижку застосовано."
    else:
        discount_message = "Знижку не застосовано."

    # Виведення чека з форматуванням f-рядків
    print("\n" + "=" * 48)
    print("                    ЧЕК")
    print("=" * 48)
    print(f"Покупець: {customer_name}")
    print("-" * 48)

    for name, item_price, item_quantity, item_sum in receipt:
        print(f"{name}: {item_price:.2f} {CURRENCY} × "
              f"{item_quantity} = {item_sum:.2f} {CURRENCY}")

    print("-" * 48)
    print(f"Категорія покупки: {purchase_category}")
    print(f"Сума до знижки:    {total:.2f} {CURRENCY}")
    print(f"Розмір знижки:     {discount_rate * 100:.0f}%")
    print(f"Економія:          {discount:.2f} {CURRENCY}")
    print(f"До сплати:         {final_total:.2f} {CURRENCY}")
    print(f"Спосіб оплати:     {payment_method}")
    print(discount_message)
    print("=" * 48)
    print("Дякуємо за покупку!")


if __name__ == "__main__":
    main()
