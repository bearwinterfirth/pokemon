import matplotlib.pyplot as plt
import pandas as pd
import random
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

def plot_data_points():
    colors=["r", "b"]
    for j in data_list:
        plt.plot(j[0],j[1],f"{colors[int(j[2])]}.")

def plot_test_points():
    for j in test_list:
        plt.plot(j[1], j[2], "g*")
    
def calculate_distance(x):
    for data_point in data_list:
        distance=np.sqrt(np.square(x[1]-data_point[0])+np.square(x[2]-data_point[1]))
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
    

classification=[]
pokemons=["Pichu", "Pikachu"]

data_list=get_datapoints_from_file()
data_list=shuffle_list(data_list)
data_list=strings_to_numbers(data_list)

test_list=get_testpoints_from_file()
test_list=strings_to_numbers(test_list)

plot_data_points()
plot_test_points()
plt.show()

for test_point in test_list:
    calculate_distance(test_point)
    
for j in range(len(test_list)):
    classification_list=[]
    data_list.sort(key = lambda x: x[j+3])
    for k in range(10):
        classification_list.append(data_list[k][2])
    s=sum(classification_list)
    if s==5:
        print(f"Unable to determine type of pokemon # {test_list[j][0]}")
    elif s > 5:
        print(f"Pokemon # {test_list[j][0]} is probably Pikachu, based on {s} of 10 nearest points.")
    else:
        print(f"Pokemon # {test_list[j][0]} is probably Pichu, based on {10-s} of 10 nearest points.")        



        

print("Now it's your turn! Please enter width and height for your pokemon!")
print("The unit is cm, and your values should be between 10 cm and 40 cm.")
width=ask_for_width()
height=ask_for_height()
result=calculate_distance([5,width,height])
print (f"Your pokemon is classified as {pokemons[result[1]]}.")



