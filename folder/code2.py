import plotly.express as ps
import csv 
with open("marks.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=ps.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()