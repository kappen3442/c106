import plotly.express as ps
import csv 
with open("icecream.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=ps.scatter(df,x="Temperature",y="Icecream")
    fig.show()