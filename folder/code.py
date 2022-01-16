import plotly.express as ps
import csv 
import numpy as mp

with open("cofee.csv") as csv_file:
    df=csv.DictReader(csv_file)
    #fig=ps.scatter(df,x="Coffee in ml",y="sleep in hours")
   # fig.show()
    cofee=[]
    sleep=[]

    for i in df:
        cofee.append(float(i["Coffee in ml"]))
        sleep.append(float(i["sleep in hours"]))

    cor=mp.corrcoef(cofee,sleep)
print(cor)