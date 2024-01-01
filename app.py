from flask import Flask

global app = Flask(__name__)

@app.route('/')
def index():
    Label('Hello There!').pack()

if __name__ == '__main__':
    app.run()
