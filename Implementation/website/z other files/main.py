from flask import Flask, request, render_template
app = Flask(__name__)

app.config.update(
    PROPAGATE_EXCEPTIONS = True
)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/company/<ticker>')
def selectcompany(ticker=None):
    return render_template('sc.html', title = ticker)

@app.route('/result')
def result():
##    return render_template('result.html')
    return ("Result")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8000')
