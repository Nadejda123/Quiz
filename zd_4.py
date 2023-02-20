#  Задание 4. Расходы на автомобиль

print('Введите расходы в месяц на следующие нужды:')

kr= float(input('Платеж по кредиту >>'))
ins= float(input('Старовка >>'))
petrol= float(input('Расходы на бензин >>'))
oil= float(input('Расходы на замену машиного масла  >>'))
tire= float(input('Шиномантаж >>'))
maint= float(input('Расходы на техобслуживание >>'))
month_cost=kr+ins+petrol+oil+tire+maint
year_cost=month_cost*12
print(f'Ежемесячная стоимость обслуживания авто составила = {month_cost} руб.')
print(f'Годовое обслуживание автомобиля составит {year_cost} руб. ')
