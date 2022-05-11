documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
}

command_list = ['p', 's', 'l', 'a', 'd', 'm', 'as', 'q']

def faq():
    print('\n Чтобы чтобы выполнить действие из правой колонки,\n введите буквенную команду из левой колонки:')
    print(
    '|-----+------------------------------------------|\n'
    '|  p  | Поиск владельца по номеру документа      |\n'
    '|-----+------------------------------------------|\n'
    '|  s  | Поиск полки по номеру документа          |\n'
    '|-----+------------------------------------------|\n'
    '|  l  | Вывести список всех документов с данными |\n'
    '|-----+------------------------------------------|\n'
    '|  a  | Добавить новый документ                  |\n'
    '|-----+------------------------------------------|\n'
    '|  d  | Удалить документ по номеру               |\n'
    '|-----+------------------------------------------|\n'
    '|  m  | Переместить документ на другую полку     |\n'
    '|-----+------------------------------------------|\n'
    '|  as | Добавить новую полку                     |\n'
    '|-----+------------------------------------------|\n'
    '|  q  | Выход                                    |\n'
    '|-----+------------------------------------------|\n'
    )

def start():
    while True:
        command = input('Введите команду из списка или q для выхода (для помощи, введите h): ')
        if command in command_list:
            return command
        elif command == 'h':
            faq()
        elif command == 'q':
            break

def document_number_request():
    while True:
        doc_number = input('Введите номер документа: ')
        if doc_number == 'q':
            break
        else:
            for doc in documents:
                if doc_number == doc['number']:
                    return doc_number
            print('Документ не найден, проверьте правильность введённого номера или введите q для выхода')

def shelf_number_request():
    while True:
            shelf_number = input(f'На какой полке разместить документ? (Доступные номера полок {list(directories.keys())}): ')
            if shelf_number in directories.keys():
                break
            print('Полка недоступна, попробуйте выбрать из представленных вариантов')
    return str(shelf_number)

def whose_doc():
    doc_number = document_number_request()
    if doc_number == None:
        print('Программа остановлена')
        return 0
    for doc in documents:
        if doc_number in doc['number']:
            print(doc['name'])
            return 1

def what_shelf():  
    doc_number = document_number_request() 
    for shl, doc in directories.items():
        if doc_number in doc:
            print(f'Документ на полке №{str(shl)}')
    return 1

def make_doc_list():
    print()
    print('Список текущих документов:')
    for doc in documents:
        print(*doc.values())

def add_doc_request():
    to_add = {'type': input('Введитте тип документа (например passport): '), 
            'number' : input('Введите номер документа: '), 
            'name' : input('Введите владельца документа: ')
    }
    shelf_number = shelf_number_request()
    return to_add, str(shelf_number)

def adding_new_doc():
    doc_data, directory_number = add_doc_request()
    documents.append(doc_data)
    directories[directory_number].append(doc_data['number'])
    print()
    print('Новый документ добавлен')
    print('-' * 25)
    print(*documents)
    print(directories)
    print('-' * 25)

def delete_doc():
    doc_number = document_number_request()
    for doc in documents:
        if doc['number'] == doc_number:
            documents.remove(doc)
    for doc in directories.values():
        if doc_number in doc:
            doc.remove(doc_number)    
    print('-' * 25)
    print(f'Документ под номером {doc_number} был успешно удалён')

def doc_move():
    doc_number = document_number_request()
    directory_number = shelf_number_request()
    for doc in directories.values():
        if doc_number in doc:
            doc.remove(doc_number)
    directories[directory_number].append(doc_number)
    print('-' * 25)
    print(f'Документ под номером {doc_number} был успешно перемещён на полку №{directory_number}')
    print('-' * 25)
    print(directories)
    
def add_new_directory():
    while True:
        new_directory_number = input('Введите номер новой полки: ')
        if new_directory_number.isdigit():
            break
        else:
            print('Номер полки должен быть числом, попробуйте ещё раз.')
    if new_directory_number not in directories.keys():
        directories.setdefault(new_directory_number,[])
        print('-' * 25)
        print(f'Новая полка под №{new_directory_number} успешно добавлена')
        print('-' * 25)
        print(f'Доступные полки: {list(directories.keys())}')
        return 1
    else:
        print('-' * 25)
        print(f'Полка под №{new_directory_number} уже существует')
        print('-' * 25)
        print(f'Доступные полки: {list(directories.keys())}')
        return 1
    

def not_foud():
    print('Команла не найдена')

commads = {'p': whose_doc,
           's': what_shelf,
           'l': make_doc_list,
           'a': adding_new_doc,
           'd': delete_doc,
           'm': doc_move,
           'as': add_new_directory,
           'q': quit
           }

while True:
    com = start()
    if com == 'q':
        break
    func = commads.get(com, not_foud)
    func()
