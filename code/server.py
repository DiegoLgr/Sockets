import time
from flask import Flask

app = Flask(__name__)
port = 5000

@app.route("/")
def index():
    text = 'Its working'
    time.sleep(2)
    return text

if __name__=="__main__":
    app.run(debug=True, host='localhost', port=port)
