import matplotlib.pyplot as plt
import numpy as np
import re

path1="datapoints.txt"
path2="testpoints.txt"
pokemons=["Pichu", "Pikachu"]

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
        distance=np.sqrt(np.square(x[1] - data_point[0]) + np.square(x[2] - data_point[1]))
        data_point.append(distance)

def find_nearest():
    data_list.sort(key = lambda x: x[-1])
    type=int(data_list[0][2])
    print(f"Pokemon number {int(test_point[0])} is classified as {pokemons[type]}.")
    
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

data_list=get_datapoints_from_file()
data_list=strings_to_numbers(data_list)

test_list=get_testpoints_from_file()
test_list=strings_to_numbers(test_list)

plot_data_points()
plot_test_points()
plt.show()

for test_point in test_list:
    calculate_distance(test_point)
    find_nearest()

print("\nNow it's your turn! Please enter width and height for your pokemon!")
print("The unit is cm, and your values should be between 10 cm and 50 cm.")

pokemon_number=5

while True:
    width=ask_for_width()
    height=ask_for_height()

    test_point=(pokemon_number,width,height)
    calculate_distance(test_point)
    find_nearest()

    try_again=input("\nDo you have more pokemons to classify? (y/n) ")
    if try_again != "y":
        break
    pokemon_number += 1    





