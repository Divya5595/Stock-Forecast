import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0]))
            #print(dates)
            prices.append(float(row[1]))
        return
 

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))
    svr_lin = SVR(kernel='linear', C=1e3).fit(dates,prices)
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
    plt.title('Support Vector Machine - Kernel Comparison')
    plt.show()
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

print ("Actual Value is: 2299.078")
get_data('aapl.csv')
print ("Data has been obtained, Training & Testing in Process")
predicted_price =   predict_prices(dates, prices, 26)
print ("Predicted Values for the RBF, Linear and Polynomial Kernel are:")
print(predicted_price) 
