from distutils import core
from statistics import correlation
import plotly.express as px
import csv
import numpy as np
def getDataSource(datapath):
    iceCreamSales = []
    temperature = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            iceCreamSales.append(float(row ["Marks In Percentage"]))
            temperature.append(float(row["Days Present"]))
    return {"x":temperature, "y":iceCreamSales}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation",correlation[0,1])
datapath = "no4.csv"
DataSource = getDataSource(datapath)
findCorrelation(DataSource)