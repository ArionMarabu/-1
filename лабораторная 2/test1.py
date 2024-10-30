money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
A = money_capital - spend
B = spend + (spend * increase)
months = 1

while A >= 0:
    A = A + salary - B
    B += B * increase
    months += 1
print("Количество месяцев, которое можно протянуть без долгов:", months)
