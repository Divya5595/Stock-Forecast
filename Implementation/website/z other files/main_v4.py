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

##@app.route('/Company_Select/SBI')
##def loading():
##    return render_template('Loading_SBI.html')

@app.route('/Output_Stock/SBI')
def result():
    # read csv file , save 5 values in variables
     with open('static\\values.csv', 'r') as inFile: 
        reader = csv.reader(inFile)
        valuelist = [row for row in reader]
    return """
    <table border="1">
    {% for line in valuelist %}
    <tr>
    {% for item in line%}
    <td>
    {{item}}
    </td>
    {% endfor %}
    </tr>
    {% endfor %}
    </table>
"""

    
##    return render_template('outputsbi.html', )


@app.route('/Analysis')
def analysis():
        return render_template('analysis.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
