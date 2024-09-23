import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import re

path1="datapoints.txt"
path2="testpoints.txt"
classification=[]


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

def plot_data_points():
    colors=["r", "b"]
    for j in main_list:
        plt.plot(j[0],j[1],f"{colors[int(j[2])]}*")
    
    

def go_through_data_points():
    pichu_distance_list=[]
    pikachu_distance_list=[]
    for data_point in main_list:
        distance=np.sqrt(np.square(test_point[1]-data_point[0])+np.square(test_point[2]-data_point[1]))
        if data_point[2]==0:
            pichu_distance_list.append(distance)
        else:
            pikachu_distance_list.append(distance)
    if min(pichu_distance_list)<min(pikachu_distance_list):
        classification.append([test_point[0], 0])
    else:
        classification.append([test_point[0], 1])
    


main_list=get_datapoints_from_file()
main_list=shuffle_list(main_list)
main_list=strings_to_numbers(main_list)

test_list=get_testpoints_from_file()
test_list=strings_to_numbers(test_list)

plot_data_points()


for test_point in test_list:
     go_through_data_points()

print(classification)
