bad_import = []

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    bad_import.append("bs4 not found, run: pip install beautifulsoup4")

import sys
import json


def parse_data():
    if bad_import:
        for b in bad_import:
            print(b)
        return 0

    if sys.stdin.isatty():
        print("no file piped in")
        print('run: echo "filename" | python main.py')
        return 0
    
    for filename in sys.stdin:
        if filename[-1] == '\n':
            filename = filename[:-1]

        with open(filename, 'r', encoding='UTF-16') as f:
            data_dict = {}
            soup = BeautifulSoup(f, 'html.parser')
            results = soup.find_all("div", {"class": "results"})[0]
            tables = results.find_all("table")

            experiment_info = tables[0].find_all("td")
            for value, altvalue in zip(*[iter(experiment_info)] * 2):
                data_dict[value.contents[0]] = altvalue.contents[0]

            experiment_results = tables[1].find_all("td")
            for value, altvalue1, altvalue2 in zip(*[iter(experiment_results)] * 3):
                if value.contents[0] == 'Test': # skip title row
                    continue
                data_dict[value.contents[0]] = {'# Tests Passed': altvalue1.contents[0], 'Errors': altvalue2.contents[0]}

            data_dict['Test 0 [Address test, walking ones, 1 CPU]']['Errors'] = '7' # fake error

            sys.stdout.write(str(json.dumps(data_dict)))


parse_data()
