from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Data load karo
df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Custermors.csv')

# Route 1 - Sabhi customers
@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(df.to_dict(orient='records'))

# Route 2 - City wise total purchase
@app.route('/city-analysis', methods=['GET'])
def city_analysis():
    result = df.groupby('City')['Purchase_Amount'].sum().reset_index()
    return jsonify(result.to_dict(orient='records'))

# Route 3 - Top 10 customers
@app.route('/top-customers', methods=['GET'])
def top_customers():
    top10 = df.nlargest(10, 'Purchase_Amount')[['Name', 'City', 'Purchase_Amount']]
    return jsonify(top10.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)