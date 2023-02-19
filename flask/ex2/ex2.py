from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/check_number', methods=['GET'])
def check_number():
    try:
        number = int(request.args.get('number'))
        if number % 2 == 0:
            result = f"{number} is an even number."
        else:
            result = f"{number} is an odd number."
    except ValueError:
        result = "Please enter an integer."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
