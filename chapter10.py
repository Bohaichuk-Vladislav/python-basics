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
