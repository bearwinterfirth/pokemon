import matplotlib.pyplot as plt
import numpy as np
import re

path1="datapoints.txt"
path2="testpoints.txt"

def get_datapoints_from_file():
    # Each row is stored as a list with 3 elements: [Width, Height, Type (0=Pichu, 1=Pikachu)]
    # These lists will be known as datapoints.
    # data_list is a nested list of all 150 datapoints.
    data_list = []
    with open(path1, "r") as datapoints:
        skip_first_line = datapoints.readline()
        for row in datapoints:
            row_list = row.strip().split(",")
            data_list.append(row_list)
        return data_list
    
def get_testpoints_from_file():
    # Each row is stored as a list with 3 elements: [Serial #, Width, Height]
    # test_list is a nested list of the 4 lists (testpoints).
    test_list = []
    with open(path2, "r") as testpoints:
        skip_first_line = testpoints.readline()
        for row in testpoints:
            row = re.sub(r"[.]", "", row, count=1)    # Remove first dot
            row = re.sub(r"[(),]", "", row)           # Remove parentheses and commas
            row_list = row.strip().split(" ")
            test_list.append(row_list)
        return test_list
    
def strings_to_numbers(list):
    # Converting all strings to floats. Some will later be converted to integers.
    for i in list:
        for j in range(len(i)):
            i[j] = float(i[j])
    return list

def plot_datapoints_and_testpoints():
    # Plotting all 150 datapoints (x=width, y=height) and 4 testpoints for visibility
    # data_list is split into pichu_list and pikachu_list for easier plotting
    pichu_list = [x for x in data_list if x[2] == 0]
    pikachu_list = [x for x in data_list if x[2] == 1]
    plt.scatter([pichu_list[j][0] for j in range(75)], [pichu_list[j][1] for j in range(75)], color = "b", label = "Pichu")
    plt.scatter([pikachu_list[j][0] for j in range(75)], [pikachu_list[j][1] for j in range(75)], color = "r")
    plt.scatter([test_list[j][1] for j in range(4)], [test_list[j][2] for j in range(4)], color = "g", marker = "*")
    plt.legend(["Pichu" , "Pikachu", "Testpoints"], loc = "upper left")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.title("Width and height of some Pokemons")
    
def calculate_distance(testpoint):
    # For each testpoint, the euclidean distances to all 150 datapoints are calculated
    # The distance between the testpoint examined at the moment, and each datapoint, is appended to the datapoint
    # (When all 4 testpoints have been examined, each datapoint will have 7 elements: [Width, Hight, Type, Distance#1, Distance#2, Distance#3, Distance#4])
    for datapoint in data_list:
        distance = np.sqrt(np.square(testpoint[1] - datapoint[0]) + np.square(testpoint[2] - datapoint[1]))
        datapoint.append(distance)

    # The data_list is sorted (from min to max) according to the latest appendices (distances)
    # The first datapoint in the sorted list is the nearest point
    # Its type (0=Pichu, 1=Pikachu) is examined, and the result is printed   
    data_list.sort(key = lambda x: x[-1])           # I learned this sorting method at https://www.geeksforgeeks.org/python-sort-list-according-second-element-sublist/
    type = int(data_list[0][2])
    print(f"Pokemon number {int(testpoint[0])}, with width {testpoint[1]} and height {testpoint[2]}, is classified as {"Pichu" if type == 0 else "Pikachu"}.")
    
def ask_for_width():
    # User inputs width of own pokemon
    while True:
        try:
            x = float(input("Width (cm)? "))
            if x < 10 or x > 50:
                raise ValueError
            else:
                break
        except ValueError:
            print("Width must be a number between 10 and 50!")
    return x

def ask_for_height():
    # User inputs height of own pokemon
    while True:
        try:
            x = float(input("Height (cm)? "))
            if x < 10 or x > 50:
                raise ValueError
            else:
                break
        except ValueError:
            print("Height must be a number between 10 and 50!")
    return x


# Part 1 - Examine the 4 testpoints by the method "nearest neighbor"

data_list = get_datapoints_from_file()
data_list = strings_to_numbers(data_list)

test_list = get_testpoints_from_file()
test_list = strings_to_numbers(test_list)
# Datapoints and testpoints are now stored as lists of floats

plot_datapoints_and_testpoints()
plt.show()

for testpoint in test_list:
    # For each of the 4 testpoints, the distance to the 150 datapoints is calculated
    # and the result (type of the nearest pokemon) is given
    calculate_distance(testpoint)


# Part 2 - User defined pokemon

print("\nNow it's your turn! Please enter width and height for your pokemon!")
print("The unit is cm, and your values should be between 10 cm and 50 cm.")

serial_number = 5    # Serial numbers 1-4 have been used, so first user defined pokemon is #5

while True:
    # User can have pokemons classified until it's not fun anymore
    width = ask_for_width()
    height = ask_for_height()

    testpoint = (serial_number,width,height)    # Same format as testpoints from test_list
    calculate_distance(testpoint)               # Calculated using same function as first 4 testpoints
    plot_datapoints_and_testpoints()
    plt.plot(width, height, "y*", markersize=10)             # Plot user's pokemon as yellow star
    plt.legend(["Pichu" , "Pikachu", "Testpoints", "Your Pokemon"], loc = "upper left")
    plt.show()

    try_again = input("\nDo you have any more pokemons to classify? (y/n) ")
    if try_again != "y":
        break
    serial_number += 1                        # Each user defined pokemon is given a unique serial number