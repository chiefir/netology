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
        command = input('Введите команду (для помощи, введите h): ')
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
                    return True, doc_number
            print('Документ не найден, проверьте правильность введённого номера или введите q для выхода')
    return False, 'Документ не найден'

def whose_doc(doc_number):
    for doc in documents:
        return doc['name']

def what_shelf(doc_number):   
    for shl, doc in directories.items():
        if doc_number in doc:
            return f'Документ на полке №{str(shl)}'


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
    while True:
        shelf_number = int(input(f'На какой полке разместить документ? (Доступны от 1 до {len(directories)}): '))
        if shelf_number > 0 and shelf_number <= len(directories):
            break
        print('Полка недоступна, попробуйте выбрать из представленных вариантов')
    return to_add, str(shelf_number)

def adding_new_doc(doc_data, directory_number):
    documents.append(doc_data)
    directories[directory_number].append(doc_data['number'])
    print('-' * 25)
    print('Новый документ добавлен!')

def delete_doc(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            documents.remove(doc)
    for doc in directories.values():
        if doc_number in doc:
            doc.remove(doc_number)    
    return f'Документ под номером {doc_number} был успешно удалён!'

com = start()

if com == 'p':
    doc_check, doc_number = document_number_request()
    if doc_check == True:
        print(whose_doc(doc_number))
    else:
        print(doc_number)
elif com == 's':
    doc_check, doc_number = document_number_request()
    if doc_check == True:
        print(what_shelf(doc_number))
    else:
        print(doc_number)
elif com == 'l':
    make_doc_list()
elif com == 'a':
    doc, shelf = add_doc_request()
    adding_new_doc(doc, shelf)
    print('-' * 24)
    print(*documents)
    print(*directories.items())
elif com == 'd':
    doc_check, doc_number = document_number_request()
    if doc_check == True:
        print('-' * 25)
        print(delete_doc(doc_number))
    else:
        print(doc_number)

