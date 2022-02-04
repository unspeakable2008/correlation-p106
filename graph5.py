import plotly.express as px
import csv
import numpy as np
def getDataSource(datapath):
    iceCreamSales = []
    temperature = []
    with open(datapath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            iceCreamSales.append(float(row ["Size of TV"]))
            temperature.append(float(row["time"]))
    return {"x":temperature, "y":iceCreamSales}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation",correlation[0,1])
datapath = "no3.csv"
DataSource = getDataSource(datapath)
findCorrelation(DataSource)