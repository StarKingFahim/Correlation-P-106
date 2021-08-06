import csv
import numpy as np

def getDateSource(data_path):
    StudentMarks=[]
    DaysPresent=[]
    with open(data_path) as f:
        csv_reader=csv.dictReader(f)

        for row in csv_reader:
            StudentMarks.append(float(row["StudentMarks"]))        
            DaysPresent.append(float(row["DaysPresent"]))
        
        return{"x":StudentMarks,"y":DaysPresent}

def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation between Size of Tv and Time Spend watching it",corelation[0,1])

def setup():
    data_path=".\Student Marks vs Days Present.csv"
    dataSource=getDateSource(data_path)
    findCorelation(dataSource)

setup()