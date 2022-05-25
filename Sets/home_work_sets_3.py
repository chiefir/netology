from tkinter import ROUND

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
    'как приготовить борщ быстро'
    ]

lenght = []
for alps in queries:
    lenght.append(len(alps.split()))

totals = {(i, lenght.count(i)) for i in lenght if lenght.count(i) > 0}
req_qty = len(queries)

print('|-------------+--------|')
print('| Кол-во слов |    %   |')
print('|-------------+--------|')

for len, count in totals:
    print(f'|      {len}      |  {round(count / req_qty * 100 , 1)}  |')
    print('|_____________+________|')