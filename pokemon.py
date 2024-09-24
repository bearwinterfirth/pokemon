import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np
import re

def get_datapoints_from_file():
    main_list=[]
    with open(path1, "r") as datapoints:
        headers=datapoints.readline()
        for row in datapoints:
            row_list=row.strip().split(",")
            main_list.append(row_list)
        return main_list
    
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
        plt.plot(j[0],j[1],f"{colors[int(j[2])]}.")

def plot_test_points():
    for j in test_list:
        plt.plot(j[1], j[2], "g*")
    
def calculate_distance(x):
    pichu_distance_list=[]
    pikachu_distance_list=[]
    for data_point in main_list:
        distance=np.sqrt(np.square(x[1]-data_point[0])+np.square(x[2]-data_point[1]))
        if data_point[2]==0:
            pichu_distance_list.append(distance)
        else:
            pikachu_distance_list.append(distance)
    if min(pichu_distance_list) < min(pikachu_distance_list):
        return [x[0], 0]
    else:
        return [x[0], 1]

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
    

path1="datapoints.txt"
path2="testpoints.txt"
classification=[]
pokemons=["Pichu", "Pikachu"]

main_list=get_datapoints_from_file()
main_list=shuffle_list(main_list)
main_list=strings_to_numbers(main_list)

test_list=get_testpoints_from_file()
test_list=strings_to_numbers(test_list)

plot_data_points()
plot_test_points()
plt.show()

for test_point in test_list:
    result=calculate_distance(test_point)
    classification.append(result)

for j in classification:
    print (f"Pokemon # {j[0]} is classified as {pokemons[j[1]]}.")

print("Now it's your turn! Please enter width and height for your pokemon!")
print("The unit is cm, and your values should be between 10 cm and 40 cm.")
width=ask_for_width()
height=ask_for_height()
result=calculate_distance([5,width,height])
print (f"Your pokemon is classified as {pokemons[result[1]]}.")



