#1 завдання
age = int(input("Введіть вік: "))
adult = age >= 18
print(adult)

if adult:
    print("Ви повнолітній")

print("Перевірку завершено")
password = input("Введіть пароль: ")
correct = password == "python123"
print(correct)

if correct:
    print("Пароль правильний")

print("Перевірку завершено")
#2 завдання
speed = int(input("Швидкість автомобіля: "))

if speed > 90:
    print("Перевищення швидкості")

print("Перевірку завершено")
#3 завдання
number = int(input("Введіть число: "))

if number > 0:
    print("Число додатне")
else:
    print("Число від'ємне або дорівнює нулю")
  score = int(input("Введіть кількість балів: "))

if score >= 90:
    print("Відмінно")
elif score >= 70:
    print("Добре")
elif score >= 50:
    print("Задовільно")
else:
    print("Незадовільно")
  #4 завдання
  money = float(input("Ваш бюджет: "))
price = float(input("Ціна товару: "))

if price > 0:
    if money >= price:
        print("Покупку можна здійснити")
    else:
        print("Недостатньо грошей")
else:
    print("Некоректна ціна")
  number = int(input("Введіть число: "))

if number >= 1 and number <= 100:
    print("Число входить у діапазон")
else:
    print("Число поза діапазоном")
#5 завдання
a = int(input("Перше число: "))
b = int(input("Друге число: "))

maximum = a if a > b else b

print("Більше число:", maximum)
number = int(input("Введіть число: "))

result = "Парне" if number % 2 == 0 else "Непарне"

print(result)
#6 завдання
season = input("Введіть номер пори року: ")

match season:
    case "1":
        print("Зима")
    case "2":
        print("Весна")
    case "3":
        print("Літо")
    case "4":
        print("Осінь")
    case _:
        print("Невідомий номер")
    day = input("Введіть день тижня: ").lower()

match day:
    case "субота" | "неділя":
        print("Вихідний день")
    case "понеділок" | "вівторок" | "середа" | "четвер" | "п'ятниця":
        print("Робочий день")
    case _:
        print("Невідомий день")
#7 завдання
point = (5, 5)

match point:
    case (0, 0):
        print("Початок координат")
    case (0, y):
        print(f"Точка на осі Y: {y}")
    case (x, 0):
        print(f"Точка на осі X: {x}")
    case (x, y) if x == y:
        print("Точка на діагоналі")
    case (x, y):
        print(f"Координати: {x}, {y}")
a = float(input("Перше число: "))
b = float(input("Друге число: "))
operation = input("Операція (+, -, *, /): ")

match operation:
    case "+":
        print("Результат:", a + b)
    case "-":
        print("Результат:", a - b)
    case "*":
        print("Результат:", a * b)
    case "/":
        if b != 0:
            print("Результат:", a / b)
        else:
            print("На нуль ділити не можна")
    case _:
        print("Невідома операція")
