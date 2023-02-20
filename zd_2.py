#Задание №2. Налог с продаж. 

sales= int(input('Введите стоимость покупки:'))
fed_nalog= sales *0.05
reg_nalog= sales *0.025
total_sales=sales+fed_nalog+reg_nalog
print (f'сумма покупки {sales} руб.')
print (f'Федеральный налог на продажу = {fed_nalog} руб.' )
print (f'Региональный налог на продажу = {reg_nalog} руб.')
print (f'Общий налог с продаж = {fed_nalog+reg_nalog} руб.')
print (f'Общая сумма продаж = {total_sales} руб. ')