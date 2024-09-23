import matplotlib.pyplot as plt
import pandas as pd
import random
import numpy as np

path1="datapoints.txt"


def get_datapoints_from_file():
    main_list=[]
    with open(path1, "r") as datapoints:
        headers=datapoints.readline().strip()
        for row in datapoints:
            row_list=row.strip().split(",")
            main_list.append(row_list)
        return main_list
    
main_list=get_datapoints_from_file()
print(main_list)