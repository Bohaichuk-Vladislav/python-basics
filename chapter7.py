 # Умовний вираз для визначення категорії покупки
    purchase_category: str = (
        "велика покупка" if total >= DISCOUNT_LIMIT
        else "звичайна покупка"
    )
