#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        newList = [0]*len(my_list)
        for i in range(len(my_list)):
            if i == idx:
                newList[i] = element
            else:
                newList[i] = my_list[i]
        return newList
