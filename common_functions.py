import matplotlib.pyplot as plt
import numpy as np
import re

path1="datapoints.txt"
path2="testpoints.txt"

def get_datapoints_from_file():
    data_list=[]
    with open(path1, "r") as datapoints:
        headers=datapoints.readline()
        for row in datapoints:
            row_list=row.strip().split(",")
            data_list.append(row_list)
        return data_list

def get_testpoints_from_file():
    test_list=[]
    with open(path2, "r") as testpoints:
        firstline=testpoints.readline()
        for row in testpoints:
            row=re.sub(r"[.]", "", row, count=1)
            row=re.sub(r"[(),]", "", row)
            row_list=row.strip().split(" ")
            test_list.append(row_list)
        return test_list
    
def strings_to_numbers(list):
    for i in list:
        for j in range(len(i)):
            i[j]=float(i[j])
    return list

def plot_data_points(data_list):
    colors=["r", "b"]
    for j in data_list:
        plt.plot(j[0],j[1],f"{colors[int(j[2])]}.")

def calculate_distance(x, data_list):
    for data_point in data_list:
        distance=np.sqrt(np.square(x[1] - data_point[0]) + np.square(x[2] - data_point[1]))
        data_point.append(distance)

def ask_for_width():
    while True:
        x=(input("Width (cm)? "))
        if x.isdigit():
            x=float(x)
            if x >= 10 and x <= 50:
                break 
        print("Width must be a number between 10 and 50!")
    return x

def ask_for_height():
    while True:
        x=(input("Height (cm)? "))
        if x.isdigit():
            x=float(x)
            if x >= 10 and x <= 50:
                break 
        print("Height must be a number between 10 and 50!")
    return x