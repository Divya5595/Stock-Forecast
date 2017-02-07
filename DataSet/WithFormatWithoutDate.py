import urllib

def main():
    base_url = "http://ichart.finance.yahoo.com/table.csv?s="
    stockstoPull = 'ONGC.NS', 'SBI', 'TCS.NS', 'ONGC.BO', 'BHEL.BO'
    output_path = "C:\Users\Divya K\Desktop\Project SVM\DataSet\Data"
   
    for eachStock in stockstoPull:
        Url = make_url(base_url, eachStock)
        print (Url)
        FileName = make_filename(output_path, eachStock)
        print (FileName)
        Output = pull_historical_data(Url, FileName)

##Make a url for each stock to pull
def make_url(base_url, ticker_symbol):
    return base_url + ticker_symbol

##Make file name and path for storing data
def make_filename(output_path, ticker_symbol):
    return output_path + ticker_symbol + ".csv"

##Pull the historical stock data
def pull_historical_data(Url, FileName):
    try:       
        urllib.urlretrieve(Url, FileName)
    except urllib.ContentTooShortError as e:
        outfile = open(FileName, "w")
        outfile.write(e.content)
        outfile.close()
       
if __name__ == "__main__":
    main()
