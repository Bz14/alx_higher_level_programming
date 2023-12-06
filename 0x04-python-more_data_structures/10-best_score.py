#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxScore = float('-inf')
    student = None
    for key, value in a_dictionary.items():
        if value > maxScore:
            maxScore = value
            student = key
    return student
