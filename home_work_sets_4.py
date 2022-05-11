stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

for k, v in stats.items():
    if v == max(stats.values()):
            print(k)
            