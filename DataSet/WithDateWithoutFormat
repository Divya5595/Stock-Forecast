#!/usr/bin/python
import yahoo_finance
import pandas as pd


def main():
    symbol = yahoo_finance.Share("GOOG")
    google_data = symbol.get_historical("2015-01-01", "2016-06-30")
    google_df = pd.DataFrame(google_data)

    # Output data into CSV
    google_df.to_csv("C:\Users\Divya K\Desktop\Project SVM\DataSet\Data\google_stock_data.csv")
    print 

if __name__ == "__main__":
    main()
