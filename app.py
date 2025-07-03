from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/ratings.html')
def ratings():
    return send_file('static/files/web-school-ratings.pdf', as_attachment=False)

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/draft')
def draft():
    return render_template('draft.html')

@app.route('/prevent-leaks.html')
def prevent_leaks():
    return send_file('static/files/web-prevent-leaks.pdf', as_attachment=False)

@app.route('/saving')
def view_pdf():
    return send_file('static/files/saving.pdf', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
