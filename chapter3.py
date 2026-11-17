 # Введення текстової інформації
    customer_name: str = str(input("Введіть ім'я покупця: ")).strip()
    if not customer_name:
        customer_name = "Покупець"

