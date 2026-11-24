price=150
quantity=4
total=quantity*price
print(total)
result=10+2*3**2
print(result)
seconds=int(input("Кількість секунд: "))
hours=seconds//3600
minutes=seconds%3600//60
rest=seconds%60
print(f"{hours} год {minutes} хв {rest} сек")
price=float(input("Ціна товару: "))
quantity1=int(input("Кількість: "))
#Розрахунок вартості зі снижками
total1=price*quantity1
discount=total1*0.10
final_price=total1-discount
print(f"До сплати: {final_price: .2f} грн")
a=int(input("Перше число: "))
b=int(input("Друге число"))
print(a+b)
number = int(input("Число: "))
is_even = number % 2 == 0
in_range = 10 <= number <= 100
valid = is_even and in_range
print(f"Допустиме число: {valid}")
balance = float(input("Баланс: "))
amount = float(input("Сума: "))
blocked = input("Заблоковано (так/ні): ") == "так"
fee = amount * 0.02
total = amount + fee
allowed = amount > 0 and balance >= total and not blocked
print(f"З комісією: {total:.2f}")
print(f"Платіж дозволено: {allowed}")

