import csv
from flask import Flask, request, render_template
app = Flask(__name__)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

@app.route('/')
def hello_world():
    return render_template('hp.html')

@app.route('/Company_Select')
def selectcompany():
        return render_template('Company_Select.html')

@app.route('/Company_Select/SBI')
def loading_SBI():
    return render_template('Loading_SBI.html')

@app.route('/Output_Stock/SBI')
def result_SBI():
    return render_template('output_SBI.html')

@app.route('/Company_Select/ONGC')
def loading_ONGC():
    return render_template('Loading_ONGC.html')

@app.route('/Output_Stock/ONGC')
def result_ONGC():
    with open('ongccsv.csv', mode='r') as infile:
      reader = csv.reader(infile)
      mydict = {rows[0]:rows[1] for rows in reader}
    print (mydict)
    return render_template('output_ONGC.html', result = mydict)


@app.route('/Company_Select/L&T')
def loading_LT():
    return render_template('Loading_LT.html')

@app.route('/Output_Stock/L&T')
def result_LT():
    with open('lntcsv.csv', mode='r') as infile:
      reader = csv.reader(infile)
      mydict = {rows[0]:rows[1] for rows in reader}
    print (mydict)
    return render_template('output_LT.html', result = mydict)

@app.route('/Company_Select/INFO')
def loading_INFO():
    return render_template('Loading_INFO.html')

@app.route('/Output_Stock/INFO')
def result_INFO():
    with open('infocsv.csv', mode='r') as infile:
      reader = csv.reader(infile)
      mydict = {rows[0]:rows[1] for rows in reader}
    print (mydict)
    return render_template('output_INFO.html', result = mydict)

@app.route('/Company_Select/TATA')
def loading_TATA():
    return render_template('Loading_TATA.html')

@app.route('/Output_Stock/TATA')
def result_TATA():
    with open('tatacsv.csv', mode='r') as infile:
      reader = csv.reader(infile)
      mydict = {rows[0]:rows[1] for rows in reader}
    print (mydict)
    return render_template('output_TATA.html', result = mydict)

@app.route('/Analysis')
def analysis():
        return render_template('analysis.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
