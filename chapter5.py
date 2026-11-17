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

