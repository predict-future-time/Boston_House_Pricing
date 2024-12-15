import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

# Load the model and scaler
app = Flask(__name__)
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Receive JSON data
    data = request.json['data']
    print(f"Input data: {data}")
    
    # Convert input to NumPy array and scale it
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)[0]
    print(f"Predicted Output: {output}")
    
    # Return prediction as JSON
    return jsonify({'prediction': output})

if __name__ == "__main__":
    app.run(debug=True)
