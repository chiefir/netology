import pathlib
import os

def main():
    files_list = os.listdir(pathlib.Path(pathlib.Path.cwd(), 'Files', 'Files to combine'))
    write_text_to_file(sort_text(files_list))

def get_text(file_name):
    with open(pathlib.Path(pathlib.Path.cwd(), 'Files', 'Files to combine', file_name), 'r') as read_file:
        text = read_file.readlines()
    return text

def sort_text(list_to_sort):
    text_dict = {}
    for file in list_to_sort:
        text_dict[file + "\n"] = get_text(file)
    return sorted(text_dict.items(), key=lambda x: len(x[1]))

def write_text_to_file(text_to_write):
    with open(input('Введите название выходного файла:') + '.txt', 'w') as out_f:
        for text in text_to_write:
            out_f.write(text[0])
            out_f.write(str(len(text[1])) + "\n")
            for lines in text[1]:
                for line in lines:
                    out_f.write(line)
            out_f.write("\n")
            
if __name__ == '__main__':
    main()
    