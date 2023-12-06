#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    for value in my_list:
        if value != search:
            newList.append(value)
        else:
            newList.append(replace)
    return newList
