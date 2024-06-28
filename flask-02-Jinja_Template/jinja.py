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
    # app.run(debug=True, port=30000)
    app.run(host= '0.0.0.0', port=80)
