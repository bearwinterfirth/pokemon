import random
import numpy as np
import matplotlib.pyplot as plt

path1="datapoints.txt"
accuracy_list = []              # The results of the 10 tries will be stored here

def get_datapoints_from_file():
    # Each row is stored as a list with 3 elements: [Width, Height, Type (0=Pichu, 1=Pikachu)]
    # These lists will be known as datapoints.
    # They are stored in two different nested lists, pichu_list and pikachu_list, based on their type
    pichu_list=[]
    pikachu_list=[]
    with open(path1, "r") as datapoints:
        skip_first_line=datapoints.readline()
        for row in datapoints:
            row_list=row.strip().split(",")
            if int(row_list[2]) == 0:
                pichu_list.append(row_list)
            else:
                pikachu_list.append(row_list)
        return pichu_list, pikachu_list

def shuffle_list(x):
    # shuffles any list
    random.shuffle(x)
    return x

def split_into_train_and_test(x):
    # both pichu_list and pikachu_list are split into train and test lists
    train_list=x[0:50]
    test_list=x[50:75]
    return train_list, test_list

def strings_to_numbers(list):
    # Converting all strings as floats. Some will later be converted to integers.
    for i in list:
        for j in range(len(i)):
            i[j]=float(i[j])
    return list

def calculate_distance(x):
    # For each testpoint, the euclidean distances to all 150 datapoints are calculated
    # Each datapoint is appended with the distance to the testpoint examined at the moment
    for datapoint in train_list:
        distance=np.sqrt(np.square(x[0] - datapoint[0]) + np.square(x[1] - datapoint[1]))
        datapoint.append(distance)

    # The train_list is sorted according to the latest appendices (distances)
    # The 10 first datapoints in the sorted list are the 10 nearest points
    train_list.sort(key = lambda x: x[-1])
    sum = 0
    for j in range(10):
        sum += int(train_list[j][2])
    return sum

def count_true_predictions(x):
    # Predicts pichu (x<5) or pikachu (x>5) and checks if the prediction is correct
    # If x=5, there will be a random choice between predicting pichu or pikachu
    # The number of correct predictions is summed
    global pred_pichu, pred_pikachu, correct_pichu, correct_pikachu
    if x == 5:
        x = random.choice([4, 6])
    if x<5:
        pred_pichu += 1
        if test_point[2]==0:
            correct_pichu +=1
    else:
        pred_pikachu += 1
        if test_point[2]==1:
            correct_pikachu +=1

for k in range(10):                                             # The program will run 10 times to get a mean accuracy value

    pichu_list, pikachu_list = get_datapoints_from_file()       # 2 lists of 75 pichu and 75 pikachu respectively

    pichu_list = shuffle_list(pichu_list)                       # shuffle both lists
    pikachu_list = shuffle_list(pikachu_list)

    pichu_train_list, pichu_test_list = split_into_train_and_test(pichu_list)   # split both lists into 50 training points and 25 testing points
    pikachu_train_list, pikachu_test_list = split_into_train_and_test(pikachu_list)

    train_list = pichu_train_list + pikachu_train_list          # merge into one training list (100 points) and one testing list (50 points)
    test_list = pichu_test_list + pikachu_test_list

    train_list = shuffle_list(train_list)                       # shuffle both training and testing lists
    test_list = shuffle_list(test_list)

    train_list = strings_to_numbers(train_list)                 
    test_list = strings_to_numbers(test_list)

    pred_pichu, pred_pikachu, correct_pichu, correct_pikachu = 0, 0, 0, 0

    for test_point in test_list:                                # predict type for all 50 test points, and check if the prediction is correct
        result=calculate_distance(test_point)
        count_true_predictions(result)

    accuracy=(correct_pichu + correct_pikachu) / (pred_pichu + pred_pikachu)
    accuracy_list.append(accuracy)                              # the accuracy is calculated and stored in the accuracy_list, which will hold 10 accuracies

[plt.plot(x+1, accuracy_list[x], "r*") for x in range(10)]      # plot the accuracy from all 10 tries
plt.xlabel("Try #")
plt.xticks(np.arange(1,11))
plt.ylabel("Accuracy (%)")
plt.ylim(0.5,1)
plt.show()

print(f"Mean accuracy is {np.mean(accuracy_list)}.\n")          # report the mean accuracy