import pprint
import sys
import json
import re

def print_info():
    for d in sys.stdin:
        data = json.loads(d)
        keys = [*data]

        n = len(sys.argv)
        if n == 1: # no args given, print whole data structure
            pprint.pprint(data)
        else: # print the params passed in as cmd args
            for i in range(1, n):
                param = sys.argv[i]
                for k in keys:
                    # matches liberally, i.e. "Test 1 " will match data: "Test 1 [Address test, own address, 1 CPU]"
                    if re.search(".*" + param + ".*", k):
                        print(k + ': ', data[k])

print_info()
