import pickle

import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify


model_path = '../models/'
model_file = 'default_logistic.bin'

with open(model_path+model_file, 'rb') as f_in:
    model = pickle.load(f_in)


app = Flask('smoking')


@app.route('/predict', methods=['POST'])
def predict():
    person = request.get_json()

    y_pred = model.predict_proba(pd.DataFrame([person]))[0, 0]
    smoker = y_pred > 0.5

    result = {
        'smoker_probability': float(y_pred),
        'smoker': bool(smoker)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=9696)