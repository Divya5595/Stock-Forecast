import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import warnings

from datetime import datetime
#warnings.filterwarnings("ignore", category=DeprecationWarning) 

import yahoo_finance
from yahoo_finance import Share
import pandas as pd


name= input("enter the stock keyword  ")
date_start = input("enter start date in the order YY-MM-DD  ")
date_end = input("enter end date in the order YY-MM-DD  ")
symbol = Share(name)
#print(symbol.get_open())
google_data = symbol.get_historical(date_start, date_end)
google_df = pd.DataFrame(google_data)

# Output data into CSV
output_path = "D:\workspace"
def make_filename(name, directory ="stockprediction"):
    return output_path + "/" + directory + "/" + name +  ".csv"
google_df.to_csv(make_filename(name,) )

print("data received")
dates = []
prices = []

model = SVR(cache_size=7000)

print("hello")

def get_data(name):
    with open(name, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            print(dates)
            prices.append(float(row[1]))
        return
  
  #
  #gaurav anex, a-17, saraswat bank, near lajja show room. ground floor.  

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))  # @UndefinedVariable
    
    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel = 'poly', C=1e3 , degree = 2 )
    svr_rbf = SVR(kernel = 'rbf', C=1e3 , gamma = 0.1)
    svr_lin.fit(dates, prices)    
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)
    
    plt.scatter(dates, prices, color='black', label = 'data')
    plt.plot(dates, svr_rbf.predict(dates), color= 'red', label ='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color= 'green', label ='linear model')
    plt.plot(dates, svr_poly.predict(dates), color= 'blue', label ='polynomial model')
    plt.xlabel('Dates')
    plt.ylabel('Price')
    plt.title('Support Vector Regresion')
    plt.show()
    
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

data_name = name + ".csv"

get_data(data_name)

predicted_price =   predict_prices(dates, prices, 26)
print (predicted_price)
print ("hello")