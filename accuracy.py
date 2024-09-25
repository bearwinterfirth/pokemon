import random
import numpy as np
import matplotlib.pyplot as plt

path1="datapoints.txt"
accuracy_list = []

def get_datapoints_from_file():
    pichu_list=[]
    pikachu_list=[]
    with open(path1, "r") as datapoints:
        headers=datapoints.readline()
        for row in datapoints:
            row_list=row.strip().split(",")
            if int(row_list[2]) == 0:
                pichu_list.append(row_list)
            else:
                pikachu_list.append(row_list)
        return pichu_list, pikachu_list

def shuffle_list(x):
    random.shuffle(x)
    return x

def split_into_train_and_test(x):
    train_list=x[0:50]
    test_list=x[50:75]
    return train_list, test_list

def strings_to_numbers(list):
    for i in list:
        for j in range(len(i)):
            i[j]=float(i[j])
    return list

def calculate_distance(x):
    for data_point in train_list:
        distance=np.sqrt(np.square(x[0] - data_point[0]) + np.square(x[1] - data_point[1]))
        data_point.append(distance)

def find_10_nearest():
    train_list.sort(key = lambda x: x[-1])
    sum = 0
    for j in range(10):
        sum += int(train_list[j][2])
    return sum

def count_true_predictions(x):
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

for k in range(10):
    pichu_list, pikachu_list = get_datapoints_from_file()

    pichu_list=shuffle_list(pichu_list)
    pikachu_list=shuffle_list(pikachu_list)

    pichu_train_list, pichu_test_list=split_into_train_and_test(pichu_list)
    pikachu_train_list, pikachu_test_list=split_into_train_and_test(pikachu_list)

    train_list=pichu_train_list + pikachu_train_list
    test_list=pichu_test_list + pikachu_test_list

    train_list=shuffle_list(train_list)
    test_list=shuffle_list(test_list)

    train_list=strings_to_numbers(train_list)
    test_list=strings_to_numbers(test_list)

    pred_pichu, pred_pikachu, correct_pichu, correct_pikachu = 0, 0, 0, 0

    for test_point in test_list:
        calculate_distance(test_point)
        result=find_10_nearest()
        count_true_predictions(result)

    accuracy=(correct_pichu + correct_pikachu) / (len(test_list))
    accuracy_list.append(accuracy)


[plt.plot(x, accuracy_list[x], "r*") for x in range(10)]
plt.ylim(0.5,1)
plt.show()

print(f"Mean accuracy is {np.mean(accuracy_list)}.\n")