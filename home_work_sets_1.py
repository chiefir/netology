geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
def visit_filtring(log):
    filtred_visits = []

    for id, visits in enumerate(log):
        for visited_country in visits.values():
            if visited_country[1] == 'Россия':
                filtred_visits.append(visits)
    return filtred_visits

new_geolog = visit_filtring(geo_logs)
print(new_geolog)
