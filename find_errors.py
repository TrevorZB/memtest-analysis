import sys
import json
import re

def find_errors():
    for d in sys.stdin:
        data = json.loads(d)

        errors = []
        for k, v in data.items():
            if re.search('Test \d', k):
                if v['Errors'] != '0':
                    errors.append({'Test Name:\t': k, 'Errors:\t\t': v['Errors']})

        if not errors:
            print('No errors found.')
        else:
            for e in errors:
                for k, v in e.items():
                    print(k, v)

find_errors()
