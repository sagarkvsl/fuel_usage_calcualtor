from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    distance = float(request.form['distance'])
    fuel_efficiency = float(request.form['fuel_efficiency'])
    price_per_liter = float(request.form['price_per_liter'])

    fuel_consumed = distance / fuel_efficiency
    cost = fuel_consumed * price_per_liter

    return render_template('index.html', result=fuel_consumed, cost=cost)

if __name__ == '__main__':
    app.run(debug=True)
