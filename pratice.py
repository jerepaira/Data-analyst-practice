from pandas import  Series,DataFrame 
import numpy as np
import random
import matplotlib.pyplot as mtb

class Students:
    # instance
    def __init__(self):
        # Generate "random numbers" (score like)
        self.scoreStudents = []
        while len(self.scoreStudents) < 10 :
            randomScore = random.randint(0,100)
            self.scoreStudents.append(randomScore)
        # DAtaFrame about scoreStudents
        self.ds = Series(data=self.scoreStudents,index=["Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
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
    
    # return the hight values obtained around curserd xd
    def mostHighScore(self):

        sortScore = self.ds.sort_values()
        highFive = sortScore[5:]

        print(highFive)
        return  highFive




# 1th Question:
# What is the student’s average test score for the entire year?
def manipulingDataStudents():
    student1 = Students()
    student2 = Students()
    student3 = Students()
    # print(student1.averageScore())
    # print(student1.secodHalfAverageScore())
    # student1.diference()
    student1.mostHighScore()
    
    
manipulingDataStudents()

