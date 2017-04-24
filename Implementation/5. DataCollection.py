#Code to get Data
#For 5 companies
#With a gap of 4 weeks each, keeping the end date const, changing start time

import datetime
from pandas_datareader import data

start_date = datetime.datetime(2017,1,30)
stockstoPull =  'ONGC.NS', 'SBI', 'TCS.NS' , 'ONGC.BO', 'BHEL.BO'

for stockTicker in stockstoPull:
    print ("Pulling Data of " + stockTicker)
    start_date = datetime.datetime(2017,1,30)
    for i in range(1): 
        start_date += datetime.timedelta(weeks=-4)
        print(i+1)
        df = data.DataReader(stockTicker, 'yahoo', start_date, '2017-01-30')
        abc = 'C:\Users\Divya K\Desktop\DataSets\\' + str(i+1)+ 'month' + stockTicker.partition('.')[0] + '.csv'
        #print (abc)
        df.to_csv(abc)

for stockTicker in stockstoPull:
    df = data.DataReader(stockTicker, 'yahoo', '2017-01-05', '2017-01-05')
    abc = 'C:\Users\Divya K\Desktop\DataSets\\' + '00Output'+  '.csv'
    #print (abc)
    df.to_csv(abc)

