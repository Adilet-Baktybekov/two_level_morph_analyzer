import csv
import sys
sys.path.append('../backend/csv_files/noun.csv')
def read_file(word):
    with open('backend/csv_files/All.csv', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter="\n")
        flag = False
        for row in file_reader:
            symbolss = row[0].split(';')
            if word == symbolss[0]:
                flag = True
                symbols_arr = symbolss[1:]
                break
        if flag:
            return symbols_arr
        else:
            return "none"
