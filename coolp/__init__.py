import argparse
import sys
import zipfile

import pandas as pd
import pytest

# def test_version():
#     assert __version__ == "0.1.0"

# with zipfile.ZipFile("/Users/lerfich/Downloads/archive.zip") as z:
#     with z.open("GlobalLandTemperaturesByMajorCity.csv") as f:
#         df = pd.read_csv(f, parse_dates=["dt"])

def start():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file', metavar='1', type=str)
    parser.add_argument('year', metavar='1', type=int)
    
    args = parser.parse_args()
    # print(args)

    db = pd.read_csv('/Users/lerfich/Downloads/archive/' + args.file, parse_dates=["dt"]) 
    db["Month"] = db['dt'].dt.month
    db["Year"] = db['dt'].dt.year

    db = db[db['Year'] == args.year].reset_index(drop = True)

    month = db.groupby("Month").max()['AverageTemperature'].idxmax() #самый жаркий месяц
    city = db.groupby("City").max()['AverageTemperature'].idxmax() #город с самой жаркой среднемесячной температурой
    temperature = db.max().AverageTemperature
    print('Month: ', month)
    print("City: ", city) 
    print("Max average temperature per month: ", temperature)

def test():
    # print(sys.version.split()[0])
    assert sys.version.split()[0] == "3.10.5"

