from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/taxonomy')
def taxonomy():
    return render_template('taxonomy.html')


@app.route('/ratings')
def ratings():
    return render_template('ratings.html')


@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/draft')
def draft():
    return render_template('draft.html')


if __name__ == '__main__':
    app.run(debug=True)
