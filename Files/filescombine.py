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
    return sorted(text_dict.items(), key=lambda x: len(x[1]))

def combine_text(text_to_write):
    with open(output_name, 'w') as out_f:
        for i in range(len(text_to_write)):
            out_f.write(text_to_write[i][0])
            out_f.write(str(len(text_to_write[i][1])) + "\n")
            for text in text_to_write[i][1]:
                for line in text:
                    out_f.write(line)
            out_f.write("\n")
            
if __name__ == '__main__':
    combine_text(sort_text(files_list))

