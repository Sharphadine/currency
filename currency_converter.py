from flask import Flask, render_template, request

app = Flask(__name__)

# Fixed exchange rates (for example only — consider using live APIs)
EXCHANGE_RATES = {
    'inr_to_xof': 7.4,
    'xof_to_inr': 1 / 7.4,
    'inr_to_usd': 0.012,
    'usd_to_inr': 1 / 0.012,
    'xof_to_usd': 0.0016,
    'usd_to_xof': 1 / 0.0016
}

@app.route('/', methods=['GET', 'POST'])
def convert_currency():
    result = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            direction = request.form['direction']
            rate = EXCHANGE_RATES.get(direction)
            if rate:
                result = round(amount * rate, 2)
                from_currency, to_currency = direction.split('_to_')
                result = f"{result} {to_currency.upper()}"
            else:
                result = "Conversion not supported."
        except ValueError:
            result = "Invalid input. Please enter a number."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)