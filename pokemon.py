import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import re

path1="datapoints.txt"
path2="testpoints.txt"


def get_datapoints_from_file():
    main_list=[]
    with open(path1, "r") as datapoints:
        headers=datapoints.readline().strip()
        for row in datapoints:
            row_list=row.strip().split(",")
            main_list.append(row_list)
        return main_list
    


def get_testpoints_from_file():
    test_list=[]
    with open(path2, "r") as testpoints:
        firstline=testpoints.readline().strip()
        for row in testpoints:
            row=re.sub(r"[.]", "", row, count=1)
            row=re.sub(r"[(),]", "", row)
            row_list=row.strip().split(" ")
            test_list.append(row_list)
        return test_list
    
def shuffle_list(x):
    random.shuffle(x)
    return x

def strings_to_numbers(list):
    for i in list:
        for j in range(len(i)):
            i[j]=float(i[j])
    return list

main_list=get_datapoints_from_file()
main_list=shuffle_list(main_list)
main_list=strings_to_numbers(main_list)

test_list=get_testpoints_from_file()
test_list=strings_to_numbers(test_list)

print(main_list)
print(test_list)