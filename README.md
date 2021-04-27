### Example Parser Useage:
```
echo "MemTest86-Report-20210425-115801.html" | python parse_data.py
```


### Example Find Errors Useage:
```
echo "MemTest86-Report-20210425-115801.html" | python parse_data.py | python find_errors.py
```
Example No Errors Output:
```
No errors found.
```
Example Errors Output:
```
Test Name:       Test 0 [Address test, walking ones, 1 CPU]
Errors:          7
```


### Example Print Info Useage:
```
echo "MemTest86-Report-20210425-115801.html" | python parse_data.py | python print_info.py
```
Example Output (No arguments given):
```
{'# Tests Passed': '14/14 (100%)',
 'CPU Selection Mode': 'Parallel (All CPUs)',
 'CPU Temperature Min/Max/Ave': '61C/87C/75C',
 'Elapsed Time': '0:27:17',
 'Memory Range Tested': '0x0 - 42F200000 (17138MB)',
 'RAM Temperature Min/Max/Ave': '-/-/-',
 'Test 0 [Address test, walking ones, 1 CPU]': {'# Tests Passed': '1/1 (100%)',
                                                'Errors': '0'},
 'Test 1 [Address test, own address, 1 CPU]': {'# Tests Passed': '1/1 (100%)',
                                               'Errors': '0'},
 'Test 10 [Bit fade test, 2 patterns, 1 CPU]': {'# Tests Passed': '1/1 (100%)',
                                                'Errors': '0'},
 'Test 11 [Random number sequence, 64-bit]': {'# Tests Passed': '1/1 (100%)',
                                              'Errors': '0'},
 'Test 12 [Random number sequence, 128-bit]': {'# Tests Passed': '1/1 (100%)',
                                               'Errors': '0'},
 'Test 13 [Hammer test]': {'# Tests Passed': '1/1 (100%)', 'Errors': '0'},
 'Test 2 [Address test, own address]': {'# Tests Passed': '1/1 (100%)',
                                        'Errors': '0'},
 'Test 3 [Moving inversions, ones & zeroes]': {'# Tests Passed': '1/1 (100%)',
                                               'Errors': '0'},
 'Test 4 [Moving inversions, 8-bit pattern]': {'# Tests Passed': '1/1 (100%)',
                                               'Errors': '0'},
 'Test 5 [Moving inversions, random pattern]': {'# Tests Passed': '1/1 (100%)',
                                                'Errors': '0'},
 'Test 6 [Block move, 64-byte blocks]': {'# Tests Passed': '1/1 (100%)',
                                         'Errors': '0'},
 'Test 7 [Moving inversions, 32-bit pattern]': {'# Tests Passed': '1/1 (100%)',
                                                'Errors': '0'},
 'Test 8 [Random number sequence]': {'# Tests Passed': '1/1 (100%)',
                                     'Errors': '0'},
 'Test 9 [Modulo 20, ones & zeros]': {'# Tests Passed': '1/1 (100%)',
                                      'Errors': '0'},
 'Test Start Time': '2021-04-25 11:58:01'}
```
```
echo "MemTest86-Report-20210425-115801.html" | python parse_data.py | python print_info.py "Test 1"
```
Example Output ("Test 1" argument given):
```
Test 1 [Address test, own address, 1 CPU]:  {'# Tests Passed': '1/1 (100%)', 'Errors': '0'}
Test 10 [Bit fade test, 2 patterns, 1 CPU]:  {'# Tests Passed': '1/1 (100%)', 'Errors': '0'}
Test 11 [Random number sequence, 64-bit]:  {'# Tests Passed': '1/1 (100%)', 'Errors': '0'}
Test 12 [Random number sequence, 128-bit]:  {'# Tests Passed': '1/1 (100%)', 'Errors': '0'}
Test 13 [Hammer test]:  {'# Tests Passed': '1/1 (100%)', 'Errors': '0'}
```
```
echo "MemTest86-Report-20210425-115801.html" | python parse_data.py | python print_info.py "Test 1 "
```
Example Output ("Test 1 " argument given (notice the space after the "1")):
```
Test 1 [Address test, own address, 1 CPU]:  {'# Tests Passed': '1/1 (100%)', 'Errors': '0'}
```
