from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_whole():
   return "We are all tests on this blessed day"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
