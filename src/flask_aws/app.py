

from flask import Flask, render_template, request

app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')

# Domestic States
@app.route('/domestic_states')
def domestic_states():
    return render_template('domestic_states.html')

# Domestic Regions
@app.route('/domestic_regions')
def domestic_regions():
    return render_template('domestic_regions.html')

# Foreign Regions
@app.route('/foreign_countries')
def foreign_regions():
    return render_template('foreign_countries.html')

# Foreign Regions
@app.route('/foreign_regions')
def foreign_countries():
    return render_template('foreign_regions.html')

# Foreign Regions
@app.route('/census')
def census():
    return render_template('census.html')

# Foreign Regions
@app.route('/term_length')
def term_length():
    return render_template('term_length.html')

# Foreign Regions
@app.route('/crime_categories')
def crime_categories():
    return render_template('crime_categories.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False)
