from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    result = None
    error = None  # To store error messages
    
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            if value < 0:
                error = "Length cannot be negative. Please enter a positive number."
            else:
                from_unit = request.form['from_unit']
                to_unit = request.form['to_unit']
                
                # Convert to meters first (base unit)
                conversions_to_meter = {
                    'millimeter': 0.001,
                    'centimeter': 0.01,
                    'meter': 1,
                    'kilometer': 1000,
                    'inch': 0.0254,
                    'foot': 0.3048,
                    'yard': 0.9144,
                    'mile': 1609.34
                }
                
                meters = value * conversions_to_meter[from_unit]
                
                # Convert from meters to target unit
                result = meters / conversions_to_meter[to_unit]
        except ValueError:
            error = "Invalid input. Please enter a valid number."
    
    return render_template('length.html', result=result, error=error)

@app.route('/weight', methods=['GET', 'POST'])
def weight_converter():
    result = None
    error = None  # To store error messages
    
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            if value < 0:
                error = "Weight cannot be negative. Please enter a positive number."
            else:
                from_unit = request.form['from_unit']
                to_unit = request.form['to_unit']
                
                # Convert to grams first (base unit)
                conversions_to_gram = {
                    'milligram': 0.001,
                    'gram': 1,
                    'kilogram': 1000,
                    'ounce': 28.3495,
                    'pound': 453.592
                }
                
                grams = value * conversions_to_gram[from_unit]
                
                # Convert from grams to target unit
                result = grams / conversions_to_gram[to_unit]
        except ValueError:
            error = "Invalid input. Please enter a valid number."
    
    return render_template('weight.html', result=result, error=error)

@app.route('/temperature', methods=['GET', 'POST'])
def temperature_converter():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            
            # Convert to Celsius first (base unit)
            if from_unit == 'celsius':
                celsius = value
            elif from_unit == 'fahrenheit':
                celsius = (value - 32) * 5/9
            elif from_unit == 'kelvin':
                celsius = value - 273.15
            
            # Convert from Celsius to target unit
            if to_unit == 'celsius':
                result = celsius
            elif to_unit == 'fahrenheit':
                result = (celsius * 9/5) + 32
            elif to_unit == 'kelvin':
                result = celsius + 273.15
        except ValueError:
            error = "Invalid input. Please enter a valid number."
    
    return render_template('temperature.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)