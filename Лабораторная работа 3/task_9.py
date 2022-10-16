salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
summ = spend
for i in range(2, months + 1):
   spend = spend * (increase + 1)
   summ = summ + spend

need_money = (summ - salary * months)

print(round(need_money))
