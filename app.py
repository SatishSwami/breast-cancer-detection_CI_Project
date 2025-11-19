import os
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(SCALER_PATH, "rb") as f:
    scaler = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["features"]
        data = np.array(data).reshape(1, -1)
        data_scaled = scaler.transform(data)
        prediction = model.predict(data_scaled)[0]
        result = "Benign (No Cancer)" if prediction == 1 else "Malignant (Cancer Detected)"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # only used for local testing
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
