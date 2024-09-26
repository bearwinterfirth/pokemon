import matplotlib.pyplot as plt
import numpy as np
import re

path1="datapoints.txt"
path2="testpoints.txt"
pokemons=["Pichu", "Pikachu"]

def get_datapoints_from_file():
    # Each row is stored as a list with 3 elements: [Width, Height, Type (0=Pichu, 1=Pikachu)]
    # These lists will be known as datapoints.
    # data_list is a nested list of all 150 datapoints.
    data_list=[]
    with open(path1, "r") as datapoints:
        skip_first_line=datapoints.readline()
        for row in datapoints:
            row_list=row.strip().split(",")
            data_list.append(row_list)
        return data_list
    
def get_testpoints_from_file():
    # Each row is stored as a list with 3 elements: [Serial #, Width, Height]
    # test_list is a nested list of the 4 lists (testpoints).
    test_list=[]
    with open(path2, "r") as testpoints:
        skip_first_line=testpoints.readline()
        for row in testpoints:
            row=re.sub(r"[.]", "", row, count=1)    # Remove first dot
            row=re.sub(r"[(),]", "", row)           # Remove parentheses and commas
            row_list=row.strip().split(" ")
            test_list.append(row_list)
        return test_list
    
def strings_to_numbers(list):
    # Converting all strings as floats. Some will later be converted to integers.
    for i in list:
        for j in range(len(i)):
            i[j]=float(i[j])
    return list

def plot_datapoints():
    # Plotting all 150 data_points (x=width, y=height) for visibility.
    # Red=Pichu, Blue=Pikachu (color determined by last element in list)
    colors=["r", "b"]
    for j in data_list:
        plt.plot(j[0],j[1],f"{colors[int(j[2])]}.")
    plt.legend(["Pichu", "Pikachu"])

def plot_test_points():
    # Plotting the 4 test_points (green stars) with the data_points for visibility
    for j in test_list:
        plt.plot(j[1], j[2], "g*")
    
def calculate_distance(testpoint):
    # For each testpoint, the euclidean distances to all 150 datapoints are calculated
    # Each datapoint is appended with the distance to the testpoint examined at the moment
    # (When all 4 testpoints have been examined, each datapoint will have 7 elements: [Width, Hight, Type, Distance#1, Distance#2, Distance#3, Distance#4])
    for datapoint in data_list:
        distance=np.sqrt(np.square(testpoint[1] - datapoint[0]) + np.square(testpoint[2] - datapoint[1]))
        datapoint.append(distance)

    # The data_list is sorted according to the latest appendices (distances)
    # The first datapoint in the sorted list is the nearest point
    # Its type (0=Pichu, 1=Pikachu) is examined, and the result is printed   
    data_list.sort(key = lambda x: x[-1])
    type=int(data_list[0][2])
    print(f"Pokemon number {int(testpoint[0])}, with width {testpoint[1]} and height {testpoint[2]}, is classified as {pokemons[type]}.")
    
def ask_for_width():
    # User inputs width of own pokemon
    while True:
        x=(input("Width (cm)? "))
        if x.isdigit():
            x=float(x)
            if x >= 10 and x <= 50:
                break 
        print("Width must be a number between 10 and 50!")
    return x

def ask_for_height():
    # User inputs height of own pokemon
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

# Datapoints and testpoints are now stored as lists of floats

plot_datapoints()
plot_test_points()
plt.show()

for testpoint in test_list:
    # For each of the 4 testpoints, the distance to the 150 datapoints is calculated
    calculate_distance(testpoint)

# Part 2 - User defined pokemon

print("\nNow it's your turn! Please enter width and height for your pokemon!")
print("The unit is cm, and your values should be between 10 cm and 50 cm.")

serial_number=5    # Serial numbers 1-4 have been used, so first user defined pokemon is #5

while True:
    width=ask_for_width()
    height=ask_for_height()

    testpoint=(serial_number,width,height)    # Same format as testpoints from test_list
    calculate_distance(testpoint)             # Calculated using same function as first 4 testpoints
    plot_datapoints()
    plt.plot(width, height, "y*")             # Plot user's pokemon as yellow star
    plt.show()

    try_again=input("\nDo you have any more pokemons to classify? (y/n) ")
    if try_again != "y":
        break
    serial_number += 1                        # Each user defined pokemon is given a unique serial number





