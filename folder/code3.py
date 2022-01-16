import plotly.express as ps
import csv 
with open("tv.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=ps.scatter(df,x="TV",y="time(hours)")
    fig.show()