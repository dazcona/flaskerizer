from flask import Flask

# APP
app = Flask(__name__)

# Static path
static_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "static"))


@app.route('/')
def index():
    return 'Hello!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)