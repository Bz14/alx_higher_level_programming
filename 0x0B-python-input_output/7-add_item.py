#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

ls = []
for i in range(1, len(sys.argv)):
    ls.append(sys.argv[i])
save_to_json_file(ls, 'add_item.json')
