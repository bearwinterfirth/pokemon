import random

path1="datapoints.txt"

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

pichu_list, pikachu_list = get_datapoints_from_file()

pichu_list=shuffle_list(pichu_list)
pikachu_list=shuffle_list(pikachu_list)

pichu_train_list, pichu_test_list=split_into_train_and_test(pichu_list)
pikachu_train_list, pikachu_test_list=split_into_train_and_test(pikachu_list)

train_list=pichu_train_list + pikachu_train_list
test_list=pichu_test_list + pikachu_test_list

train_list=shuffle_list(train_list)
test_list=shuffle_list(test_list)

