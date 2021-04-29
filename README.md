### Parse the HTML into a python dictionary / JSON object:
```
echo "MemTest86-Report-20210425-115801.html" | python parse_data.py
```


### Pipe the parser output into error_info.py to check for errors / get info on errors:
```
echo "MemTest86-Report-20210429-131049.html" | python parse_data.py | python error_info.py
```


### Pipe the error_info.py output into a log file:
```
echo "MemTest86-Report-20210429-131049.html" | python parse_data.py | python error_info.py > error_summary.txt
```


### Pipe the parser output into print_info.py to get information about the experiment:
#### Passing no args to print_info.py prints the entire JSON object
#### Passing args to print_info.py prints specific data
```
echo "MemTest86-Report-20210425-115801.html" | python parse_data.py | python print_info.py "Test 1"
```
