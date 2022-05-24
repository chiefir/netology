files_list = ['1.txt', '2.txt']
output_name = input('Введите название выходного файла:') + '.txt'

def get_text(file_name):
    with open(file_name, 'r') as read_file:
        text = read_file.readlines()
    return text

def sorting_text(file_list):
    text_list = []
    for file in file_list:
        text_list.append(get_text(file))
    text_dict = {}
    for length in text_list:
        text_dict.setdefault(len(length), length)
    return sorted(text_dict.items())

with open(output_name, 'w') as out_file:
    pre_out_text = sorting_text(files_list)
    print(pre_out_text)



