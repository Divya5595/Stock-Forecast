##from flask import Flask, render_template
##app = Flask(__name__)
##
##@app.route('/result')
##def result():
##   dict = {'phy':50,'che':60,'maths':70}
##   return render_template('out.html', result = dict)
##
##if __name__ == '__main__':
##   app.run(debug=True)

import csv
from flask import Flask, request, render_template
app = Flask(__name__)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

@app.route('/')
def hello_world():
    return('Hello World!!!!')

@app.route('/csv')
def csv_maker():
      dict = {'phy':50,'che':60,'maths':70}
      return render_template('out.html', result = dict)
   
##     mydict = {'phy':50,'che':60,'maths':70}
####    with open('values.csv', mode='r') as infile:
####        reader = csv.reader(infile)
####        with open('values_new.csv', mode='w') as outfile:
####            writer = csv.writer(outfile)
####        mydict = dict((rows[0],rows[1]) for rows in reader)
####        print (mydict)
##
##     return render_template('out.html', result = mydict)
##
##
##
##
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
