 # Додаткова перевірка логічними операторами and, or, not
    if (discount_rate > 0 and final_total < total) or not customer_name:
        discount_message: str = "Знижку застосовано."
    else:
        discount_message = "Знижку не застосовано."
