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