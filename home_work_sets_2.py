ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

list_of_id_sets = []
for id_sets in ids.values():
    list_of_id_sets.extend(id_sets)


print(set(list_of_id_sets))
