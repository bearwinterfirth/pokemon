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
        firstline = testpoints.readline()
        for row in testpoints:
            row = re.sub(r"[.]", "", row, count=1)
            row = re.sub(r"[(),]", "", row)
            row_list = row.strip().split(" ")
            test_list.append(row_list)
        return test_list
    
def strings_to_numbers(list):
    # Converting all strings as floats. Some will later be converted to integers.
    for i in list:
        for j in range(len(i)):
            i[j] = float(i[j])
    return list

def plot_datapoints_and_testpoints():
    # Plotting all 150 datapoints (x=width, y=height) and 4 testpoints for visibility
    # Data_list is split into pichu_list and pikachu_list for easier plotting
    pichu_list = [x for x in data_list if x[2] == 0]
    pikachu_list = [x for x in data_list if x[2] == 1]
    plt.scatter([pichu_list[j][0] for j in range(75)], [pichu_list[j][1] for j in range(75)], color = "b", label = "Pichu")
    plt.scatter([pikachu_list[j][0] for j in range(75)], [pikachu_list[j][1] for j in range(75)], color = "r")
    plt.scatter([test_list[j][1] for j in range(4)], [test_list[j][2] for j in range(4)], color = "g", marker = "*")
    plt.legend(["Pichu" , "Pikachu", "Testpoints"], loc="upper left")
    plt.xlabel("Width")
    plt.ylabel("Height")
    
def calculate_distance(testpoint):
    # For each testpoint, the euclidean distances to all 150 datapoints are calculated
    # Each datapoint is appended with the distance to the testpoint examined at the moment
    # (When all 4 testpoints have been examined, each datapoint will have 7 elements: [Width, Hight, Type, Distance#1, Distance#2, Distance#3, Distance#4])
    for datapoint in data_list:
        distance = np.sqrt(np.square(testpoint[1] - datapoint[0]) + np.square(testpoint[2] - datapoint[1]))
        datapoint.append(distance)

    # The data_list is sorted (min to max) according to the latest appendices (distances)
    # The 10 first datapoints in the sorted list are the 10 nearest points
    # Their types (0=Pichu, 1=Pikachu) are added together, which yields a sum between 0 (only pichus) and 10 (only pikachus)   
    data_list.sort(key = lambda x: x[-1])
    sum = 0
    for j in range(10):
        sum += int(data_list[j][2])
    return sum

def present_result(x):
    # If the sum is < 5, there are more 0's than 1's, so the majority vote is for Pichu
    # Vice versa for Pikachu (>5)
    # If the sum is 5 exactly, we're unable to determine the type.
    if x == 5:
        print(f"Unable to classify Pokemon number {int(testpoint[0])}, with width {int(testpoint[1])} and height {int(testpoint[2])}.")
        print(f"The vote is 5-5.\n")
    else:
        print(f"Pokemon number {int(testpoint[0])}, with width {testpoint[1]} and height {testpoint[2]} is classified as {"Pichu" if x < 5 else "Pikachu"}.")
        print(f"The vote is {max(x, 10-x)}-{min(x, 10-x)}.\n")
    
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

def draw_circle(center, radius):
    # Draw circle (for visibility) with center=(user's width and height), and radius=distance to 10th nearest point
    # The 10 nearest points are now within (or on) the circle
    x = np.linspace(0, 2*np.pi)
    plt.plot(radius*np.cos(x)+center[0], radius*np.sin(x)+center[1])
    plt.axis("equal")


# Part 1 - Examine the 4 testpoints by the method "10 nearest neighbors"

data_list = get_datapoints_from_file()
data_list = strings_to_numbers(data_list)

# Datapoints and testpoints are now stored as lists of floats

test_list = get_testpoints_from_file()
test_list = strings_to_numbers(test_list)

plot_datapoints_and_testpoints()
plt.show()

for testpoint in test_list:
    # For each of the 4 testpoints, the distance to the 150 datapoints is calculated
    # and we get the result by majority vote from 10 nearest points
    result = calculate_distance(testpoint)    # result is the sum between 0 and 10
    present_result(result)                  # the result is presented to the user


# Part 2 - User defined pokemon
    
print("Now it's your turn! Please enter width and height for your pokemon!")
print("The unit is cm, and your values should be between 10 cm and 50 cm.")

serial_number=5         # Serial numbers 1-4 have been used, so first user defined pokemon is #5

while True:
    width = ask_for_width()
    height = ask_for_height()

    testpoint = (serial_number,width,height)   # Same format as testpoints from test_list
    result = calculate_distance(testpoint)     # Calculated using same function as first 4 testpoints
    present_result(result)
   
    plt.plot(width, height, "y*")            
    plot_datapoints_and_testpoints()
    draw_circle((width, height), data_list[9][-1])           # draw circle which shows 10 nearest points from user's pokemon
    plt.plot(width, height, "y*", markersize = 10)             # Plot user's pokemon as yellow star
    plt.legend(["Your Pokemon", "Pichu" , "Pikachu", "Testpoints", "10-NN"], loc="upper left")
    plt.show()

    try_again = input("Do you have any more pokemons to classify? (y/n) ")
    if try_again != "y":
        break
    serial_number += 1                       # Each user defined pokemon is given a unique serial number






