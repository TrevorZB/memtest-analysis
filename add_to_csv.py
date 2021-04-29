import csv
import sys


def add_to_csv():
    data = json.loads(d)
    




    n = len(sys.argv)
    if n == 1:
        print('No column titles given')
        print('usage: "csv_file_name" | python create_base_csv.py "column_title_1" "column_title_2" ... "column_title_n"')
        return
    else:
        titles = []
        for i in range(1, n):
            titles.append(sys.argv[i])            

    for filename in sys.stdin:
        if filename[-1] == '\n':
            filename = filename[:-1]

        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f, delimeter=',')
            writer.writerow(titles)
            print(filename + " successfully created.")
            print("Following titles were successfully added to " + filename + ":")
            print(titles)

