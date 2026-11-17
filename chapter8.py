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
