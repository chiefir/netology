files_list = ['1.txt', '2.txt']
output_name = input('Введите название выходного файла:') + '.txt'

def get_text(file_name):
    with open(file_name, 'r') as read_file:
        text = read_file.readlines()
    return text

def sort_text(list_to_sort):
    text_dict = {}
    for file in list_to_sort:
        text_dict[file + "\n"] = get_text(file)
    text_dict_to_sort = {}
    for name, text in text_dict.items():
        text_dict_to_sort[str(len(text)) + "\n"] = {name: text}
    return sorted(text_dict_to_sort.items())

def combine_text(text_to_write):
    with open(output_name, 'w') as out_f:
        for i in range(len(text_to_write)):
            out_f.write(str(*text_to_write[i][1].keys()))
            out_f.write(str(text_to_write[i][0]))
            for text in text_to_write[i][1].values():
                for line in text:
                    out_f.write(line)
            out_f.write("\n")
            
if __name__ == '__main__':
    combine_text(sort_text(files_list))
