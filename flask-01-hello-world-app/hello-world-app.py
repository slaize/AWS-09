from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/secondpage')
def second_page():
    return 'This is second page'

@app.route('/thirdpage')
def third_page():
    return 'This is third page'

@app.route('/fourth/<string:id>')
def fourth_page(id):
    return f'Id of this page is {id}'


if __name__ == "__main__":
    # app.run(debug=True, port=30000)
    app.run(host= '0.0.0.0', port=8080)

