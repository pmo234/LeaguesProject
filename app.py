from flask import Flask, render_template
from controllers.leagues_controller import leagues_blueprint
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(leagues_blueprint)
