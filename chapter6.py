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
