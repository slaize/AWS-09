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

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='3.83.237.57', port=80)
