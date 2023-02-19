from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def current_time():
    now = datetime.now()
    formatted_time = now.strftime("%A, %B %d, %Y %X")
    return f"The current date time is {formatted_time}"

if __name__ == '__main__':
    app.run()
