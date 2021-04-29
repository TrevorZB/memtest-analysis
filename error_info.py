import pprint
import sys
import json
import re

def error_info():
    for d in sys.stdin:
        data = json.loads(d)

        error_info = []
        if 'Errors' in data:
            errors = data['Errors']
            for error in errors:
                address = re.search('Address: ([^,]*),', error).group(1)
                hex_expected = re.search('Expected: ([^,]*),', error).group(1)
                hex_actual = re.search('Actual: (.*)', error).group(1)
                bin_expected = f'{int(hex_expected, 16):0>32b}'
                bin_actual = f'{int(hex_actual, 16):0>32b}'

                b_e = int(bin_expected, 2)        
                b_a = int(bin_actual, 2)

                flip = b_e ^ b_a
                index = f'{flip:0>32b}'.index('1')
                flip_str = f'flipped from {bin_expected[index]} to {bin_actual[index]} at bit position {index} of the pattern'

                if len(error_info) == 0:
                    dist_info = 'N/A'
                else:
                    prev_addr = error_info[-1]['___address']
                    dist = abs(int(address, 16) - int(prev_addr, 16))
                    if dist > 1000000:
                        measure = 'MB'
                        dist /= 1000000
                    else:
                        measure = 'BYTES'
                    dist_info = f'absolute distance from previous error address: {dist} {measure}'

                error_info.append({'___address': address,
                                   'hex_expect': hex_expected,
                                   'hex_actual': hex_actual,
                                   'bin_expect': bin_expected,
                                   'bin_actual': bin_actual,
                                   '_flip_info': flip_str,
                                   '_dist_info': dist_info
                                   })
        else:
            print('no errors found')
            return

        print('Last ' + str(len(error_info)) + ' Errors:')
        print('')
        for i, info in enumerate(error_info):
            print("Error " + str(i) + ":")
            for k, v in info.items():
                print(k + ":\t\t" + v)
            print('')

        min_addr = min(error_info, key=lambda e: int(e['___address'], 16))
        max_addr = max(error_info, key=lambda e: int(e['___address'], 16))
        r = str((int(max_addr['___address'], 16) - int(min_addr['___address'], 16)) / 1000000)

        print('')
        print('Max Contiguous Errors: ' + data['Max Contiguous Errors'])
        print('Address range (Last 10 Errors Table): ' + min_addr['___address'] + " - " + max_addr['___address'] + ' (' + r + ' MB)')
        print('Lowest Error Address: ' + data['Lowest Error Address'])
        print('Highest Error Address: ' + data['Highest Error Address'])


error_info()
