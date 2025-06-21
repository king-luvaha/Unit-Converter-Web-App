# Unit Converter Web Application

A responsive web application that converts between different units of measurement (length, weight, and temperature) built with Python Flask.

![[Unit Converter.gif]]

## Features

- **Three Conversion Types**:
  - 📏 Length: millimeter, centimeter, meter, kilometer, inch, foot, yard, mile
  - ⚖️ Weight: milligram, gram, kilogram, ounce, pound
  - 🌡️ Temperature: Celsius, Fahrenheit, Kelvin

- **Professional UI**:
  - Clean, modern interface
  - Side-by-side form and results layout
  - Responsive design (works on mobile/desktop)
  - Input validation with error messages

- **Technical Highlights**:
  - Python backend with Flask
  - Jinja2 templating
  - No database required
  - Client-side form persistence

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## Installation

### Option 1: Clone Repository
```bash
git clone https://github.com/yourusername/unit-converter.git
cd unit-converter
```

### Option 2: Manual Setup
1. Create project folder:
   ```bash
   mkdir unit-converter
   cd unit-converter
   ```

2. Create the required folder structure:
   ```
   unit-converter/
   ├── app.py
   ├── templates/
   │   ├── base.html
   │   ├── index.html
   │   ├── length.html
   │   ├── weight.html
   │   └── temperature.html
   └── static/
       └── style.css
   ```

3. Copy the code files into their respective locations.

## Setup

1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv/Scripts/activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

## Running the Application

Start the development server:
```bash
python app.py
```

The application will be available at:
```
http://localhost:5000
```

## Project Structure

```
unit-converter/
├── app.py                # Main application file
├── static/
│   └── style.css         # All CSS styles
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── length.html       # Length converter
│   ├── weight.html       # Weight converter
│   └── temperature.html  # Temperature converter
├── README.md             # This file
└── requirements.txt      # Generated with `pip freeze > requirements.txt`
```

## Usage Guide

1. **Homepage**:
   - Select the type of conversion you need

2. **Converter Pages**:
   - Enter the value to convert
   - Select source and target units
   - Click "Convert" button
   - View results displayed on the right side

3. **Error Handling**:
   - Negative values are blocked for length/weight
   - Invalid inputs show clear error messages

## Deployment

To deploy this application to a production environment:

1. For simple hosting:
   - PythonAnywhere
   - Heroku (with Procfile)
   - Render.com

2. For production WSGI servers:
   - Gunicorn
   - uWSGI
   - Waitress

Example Gunicorn command:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Customization

To modify the application:

1. Add new units:
   - Update the conversion logic in `app.py`
   - Add new options to the select menus in templates

2. Change styling:
   - Edit `static/style.css`
   - Color scheme uses CSS variables for easy theming

3. Add new conversion types:
   - Create new route in `app.py`
   - Add new template file
   - Update navigation in `base.html`

## Troubleshooting

Common issues and solutions:

**Issue**: ModuleNotFoundError: No module named 'flask'
- **Solution**: Ensure you activated the virtual environment and ran `pip install flask`

**Issue**: TemplateNotFound
- **Solution**: Verify all HTML files are in the `templates` folder (name must be exact)

**Issue**: Port already in use
- **Solution**: Change port in `app.py`:
  ```python
  if __name__ == '__main__':
      app.run(debug=True, port=5001)
  ```

## License

This project is open source and available under the [MIT License](LICENSE).

---

