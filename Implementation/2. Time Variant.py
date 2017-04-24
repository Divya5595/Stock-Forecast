import pandas as pd
import math, datetime
import time
import numpy as np
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import cross_validation, preprocessing, svm
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC
from matplotlib import style
import datetime
from pandas_datareader import data

style.use ('ggplot')

#Setting Companies
#stockstoPull =  ['SBIN.NS' , 'ONGC.NS', 'LTI.NS', 'TCS.NS', 'INFY.NS']
def Set_Ticker():
    global stockTicker
    stockTicker = 'ONGC.NS'
    return 

def Actual_Value():
    #Actual Value
    global df
    print("The Actual Closing Value is Displayed below")
    df = data.DataReader(stockTicker, 'yahoo', '2017-04-21', '2017-04-24')
    ao=df['Close']
    print (str(ao))
    return

def Set_Date():
    #Setting Date
    global end_date
    global start_date
    end_date = datetime.datetime(2017,4,24)
    start_date = end_date
    return

def Add_Features_x():
    #Create Features - X
    global df
    df ['OC_Change'] = (df['Close']-df['Open']/df['Open']*100)
    df ['HL_Change'] = (df['High']-df['Low']/df['Low']*100)
    df = df[['Close', 'HL_Change', 'OC_Change', 'Volume']]
    return

def Forcast_Values():
    #Forecast
    global forecast_out
    global forecast_col
    forecast_col = 'Close'
    forecast_out = int(math.ceil(0.01*len(df)))
    return

def Add_Features_y():
    #Label - y
    df['label'] = df[forecast_col].shift(-forecast_out)
    df.dropna(inplace=True)
    return

def Setup_Validate_data():
    #Set X and y    
    global y
    global X
    global X_train, X_test, y_train, y_test
    X = np.array(df.drop(['label'],1))
    y = np.array(df['label'])
    #Split Training and Testing Data
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)
    return

def Set_Model():
    #Set Model for ML
    global clf
    clf = LinearRegression()
    #clf = svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',max_iter=-1, probability=False, random_state=None, shrinking=True,tol=0.001, verbose=False)
    #clf = svm.SVC(C=100000,kernel='rbf')
    #clf = svm.SVR()
    clf.fit(X_train, y_train)
    return

def get_Accuracy():
    #Accuracy of Test Data
    global accuracy
    accuracy = clf.score(X_test, y_test)
    return()

def Prediction():
    #Predict Next Values
    global X
    X = X[:-forecast_out]
    global X_lately
    global forecast_set
    X_lately = X[-forecast_out:]
    forecast_set = clf.predict(X_lately)

def Data_frame_Create():
    #Creat a DataFrame 
    global df
    df = data.DataReader(stockTicker, 'yahoo', start_date, end_date)
    return

Set_Ticker()
Actual_Value()

#Setting Date
Set_Date()

#Gap of 1 month in time
n = int(input("Enter the No. of Years in Months:"))

#Output Table Header
print ('Company\t Days\t Predicted Values')

for i in range(n): 
    start_date += datetime.timedelta(weeks=-4)

    #Creat a DataFrame
    Data_frame_Create()        
    
    #Create Features - X
    Add_Features_x()

    #Forecast
    Forcast_Values()

    #Label - y
    Add_Features_y()

    #Split Training and Testing Data
    Setup_Validate_data()

    #Set Model for ML
    Set_Model()

    #Accuracy of Test Data
    get_Accuracy()

    #Predict Next Values
    Prediction()
        
    print (stockTicker.partition('.')[0] +'\t'+ str(len(X)) +'\t'+ str(forecast_set))
