from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)      # Enables frontend → backend communication

# ================================
# LOAD MODEL AND SCALER SAFELY
# ================================
# Use RAW STRING r"" to avoid unicode errors
model = pickle.load(open(r"C:\Users\shrut\OneDrive\Desktop\BreastCancerFrontend\model.pkl", "rb"))
scaler = pickle.load(open(r"C:\Users\shrut\OneDrive\Desktop\BreastCancerFrontend\scaler.pkl", "rb"))

# ================================
# PREDICTION API
# ================================
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json["features"]        # Read input features
        data = np.array(data).reshape(1, -1)   # Convert to array
        data_scaled = scaler.transform(data)   # Scale inputs
        prediction = model.predict(data_scaled)[0]

        result = "Benign (No Cancer)" if prediction == 1 else "Malignant (Cancer Detected)"

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# ================================
# RUN FLASK SERVER
# ================================
if __name__ == "__main__":
    app.run(debug=True)
