bad_import = []

try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    bad_import.append("bs4 not found, run: pip install beautifulsoup4")

import sys
import json
import pprint


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

            for table in tables:
                info = table.find_all('td')
                if len(info) % 2 == 0:
                    for value, altvalue in zip(*[iter(info)] * 2): # handles results tables that have 2 columns (ex: result meta data tables)
                        data_dict[value.contents[0]] = altvalue.contents[0]
                elif len(info) % 3 == 0:
                    for value, altvalue1, altvalue2 in zip(*[iter(info)] * 3): # handles results tables that have 3 columns (ex: test table)
                        data_dict[value.contents[0]] = [altvalue1.contents[0], altvalue2.contents[0]]
                else: # handles results tables that have 1 column (ex: Last 10 Errors table)
                    for td in info:
                        contents = td.contents[0]
                        if contents == "Last 10 Errors":
                            data_dict['Errors'] = []
                        else:
                            data_dict["Errors"].append(contents)

            sys.stdout.write(str(json.dumps(data_dict)))


parse_data()
