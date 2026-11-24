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
