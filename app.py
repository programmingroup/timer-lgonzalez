from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def get_server_time():
    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    return (f"<div style='text-align: center; margin-top: 40%; font-size: 20px; font-family: \"Helvetica\";'>"
            f"<h1>Current Time</h1>"
            f"<p><strong>Date: </strong>{date}</p>"
            f"<p><strong>Time: </strong>{time}</p></div>")

if __name__ == '__main__':
    app.run()