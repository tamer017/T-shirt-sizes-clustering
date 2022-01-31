from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
color=["green","cyan","magenta","orange","black","purple","brown","beige"]
def plot(k,data,Centers):
    for i in range(k):
        tempData=data[data["column 7"]==i+1]
        plt.scatter(tempData["pca 1"],tempData["pca 2"],c=color[i])
    plt.scatter(Centers["pca 1"],Centers["pca 2"],c='red')
    plt.xlabel('pca 1')
    plt.ylabel('pca 2')
    plt.show()
    



# import random as random
# import pandas as pd
# data=pd.read_csv('group5.csv',names=["column 1","column 2","column 3","column 4","column 5"])
# random.seed(5)
# # len(data.index)) number of rows
# k=5
# randomlist = random.sample(range(0, len(data.index)), k)
# Centers=data.loc[randomlist]
# # change the row indexes tobe the same as new centers list
# Centers.index=list(range(1,k+1))
# print(Centers)