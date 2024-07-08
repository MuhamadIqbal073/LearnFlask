from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<id>/')
def hello_world(id):  # put a
    print(id)# pplication's code here
    return render_template('main.html')

@app.route('/about/<about>')
def new(about):
    print(about)
    return render_template('coba.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


if __name__ == '__main__':
    app.run(debug=True)
