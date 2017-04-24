from flask import Flask, render_template
import csv
app = Flask(__name__)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

@app.route('/result')
def result():
   with open('mycsvfile.csv', mode='r') as infile:
      reader = csv.reader(infile)
      mydict = {rows[0]:rows[1] for rows in reader}
   print (mydict)
   return render_template('result.html', result = mydict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')

