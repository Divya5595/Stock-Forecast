import csv
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
import matplotlib.patches as mpatches


# (Year, month, day) tuples suffice as args for quotes_historical_yahoo
##date1 = (2004, 2, 1)
##date2 = (2004, 4, 12)
dates = []
prices = []
ddd = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            #ddd = dates.append(int(row[0]))
            dates.append(int(row[0].split('-')[0]))
            print(dates)
            prices.append(float(row[1]))
        return
#.split('-')[0]
#gaurav anex, a-17, saraswat bank, near lajja show room. ground floor.  

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12


def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))
    svr_lin = SVR(kernel='linear', C=1e3).fit(dates,prices)
    svr_poly = SVR(kernel = 'poly', C=1e3 , degree = 2 )
    svr_rbf = SVR(kernel = 'rbf', C=1e3 , gamma = 0.1)
    svr_lin.fit(dates, prices)    
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)
    lw=2
    plt.scatter(dates, prices, color='black', lw=lw, label = 'data')
    plt.plot(dates, svr_rbf.predict(dates), color= 'red', lw=lw, label ='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color= 'green',lw=lw,  label ='linear model')
    plt.plot(dates, svr_poly.predict(dates), color= 'blue',lw=lw, label ='polynomial model')
    plt.xlabel('Dates (Date)')
    plt.ylabel('Open Price (INR)')
    plt.suptitle('Support Vector Machine', fontsize=16)
    plt.title('Ticker: AAPL \n Time Period: 20th Jan to 27th Jan 2016', fontsize=10)
    redp = mpatches.Patch(color='red', label='RBF Model')
    greenp = mpatches.Patch(color='green', label='LR')
    bluep = mpatches.Patch(color='blue', label='SVM')
    plt.legend(handles=[redp, greenp, bluep])                          
    plt.show()
    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('aapll.csv')
predicted_price =   predict_prices(dates, prices, 26)
print(predicted_price) 
