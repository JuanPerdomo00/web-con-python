from flask import Flask, render_template

app = Flask(__name__)


# rutas
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def acerca_de():
    return render_template('acerca_de.html')


if __name__ == "__main__":
    app.run(debug=True)
