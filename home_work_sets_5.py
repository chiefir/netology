get_list = ['2018-01-01', 'yandex', 'cpc', 100]
if len(get_list) < 2:
    print('Для формирования словаря необходим список минимум из 2 элементов')
else:
    get_copy_list = get_list[:]
    new_dict = {get_copy_list[-1], get_copy_list[-2]}

    for i in range(-3, -len(get_copy_list) - 1, -1):
        new_dict = {get_copy_list[i] : new_dict}

print(new_dict)