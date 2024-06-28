from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', number1=5, number2=6)

@app.route('/sum')
def calculate_sum():
    number1 = 5
    number2 = 6
    total = number1 + number2
    return render_template('body.html', number1=number1, number2=number2, sum=total)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='3.83.237.57', port=80)
