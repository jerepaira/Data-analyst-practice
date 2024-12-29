from pandas import  Series,DataFrame
import pandas as pd 
import numpy as np
import random
import matplotlib.pyplot as plt
import math

class Students:
    # instance
    def __init__(self):
        # Generate "random numbers" (score like)
        self.scoreStudents = []
        self.scoreStudents2 = []
        # score one
        while len(self.scoreStudents) < 10 :
            randomScore = random.randint(0,100)
            self.scoreStudents.append(randomScore)
        # DAtaFrame about scoreStudents
        self.ds = Series(data=self.scoreStudents,index=["Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
        # score two
        while len(self.scoreStudents2) < 10 :
            randomScore2 =random.randint(40,60)
            self.scoreStudents2.append(randomScore2)
        self.ds2 = Series(data=self.scoreStudents2,index=["Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
        scoreStudents3 = np.random.randint(0,100,10)
        self.ds3 = Series(data=scoreStudents3, index=["Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
    #mean 
    def averageScore(self): 
        idMax = self.ds.idxmax()
        maxScore = np.max(self.ds)
        print(f"the max score is {idMax} : %{maxScore}")
        means = self.ds.mean()      
        return means,maxScore,idMax

    # 1th mean
    def firstHalfAverageScore(self):
        fisrtHalfMean = self.ds[:5].mean()
        return fisrtHalfMean
    # 2th mean
    def secodHalfAverageScore(self):
        secodHalfMean = self.ds[5:].mean()
        return secodHalfMean
    # 3th diference
    def diference(self):
        diference1 = self.secodHalfAverageScore() - self.firstHalfAverageScore()
        if (diference1) > 0 :
            print(f"the student increment your score %{np.round(diference1,3)}")
        else:
            print(f"the student decrement your score %{np.round(diference1,3)}")
    
    # return the hight values obtained around the course xd
    def mostHighScore(self):

        sortScore = self.ds.sort_values()
        highFive = sortScore[5:]

        print(highFive)
        return  highFive

    def ajustingScore(self):
        ajust = (80 - self.ds2.mean())
        self.ds = self.ds + ajust
        return self.ds
    
    def modificateBaseSerie(self):
        self.ds3 = self.ds3.div(10)
        print(self.ds3)
        # self.ds3 = self.ds3.astype(str)
        # self.ds3 = self.ds3.astype(pd.StringDtype())
        self.ds3 = self.ds3.astype(np.int8)
        return self.ds3
        
# 1th Question:
# What is the student’s average test score for the entire year?
def manipulingDataStudents():
    student1 = Students()
    student2 = Students()
    student3 = Students()
    # print(student1.averageScore())
    # print(student1.secodHalfAverageScore())
    # student1.diference()
    # # student1.mostHighScore()
    # print(student1.ds)
    
    # print(student1.modificateBaseSerie())
    
manipulingDataStudents()


def ss():
    list =[]
    while len(list) < 10 :
        rr = random.randint(0,100)
        list.append(rr)
    
    dd = Series(data=list,index=['a','b','c','d','e','f','g','h','i','j'])
    return dd
    
    
# 4 exercise (i change the  line becouse the previous code is a shit )

class descriptive():
    def __init__(self):
        scoreSerie = np.random.normal(0,100,100_000)
        self.descriptiveSerie = Series(data=scoreSerie,dtype=np.float64)
   
        
    def statistic(self):
        dates =self.descriptiveSerie.describe()
        idMin=self.descriptiveSerie.loc[self.descriptiveSerie == self.descriptiveSerie.min()]
        plusId = idMin.max()*5
        return dates,plusId
    
    
    def graph(self):
        self.descriptiveSerie.plot(kind='hist', bins=60, alpha=0.7, color='red')
        plt.title('Histogram of Descriptive Series')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()
        

a=descriptive()

print(a.graph())
