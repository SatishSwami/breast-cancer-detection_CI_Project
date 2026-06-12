# 🩺 Breast Cancer Detection System

An AI-powered Breast Cancer Detection System developed using Machine Learning and Flask. This application predicts whether a breast tumor is **Benign** or **Malignant** based on diagnostic features provided by the user.

## 📌 Project Overview

Breast cancer is one of the most common cancers affecting women worldwide. Early detection significantly increases the chances of successful treatment.

This project leverages Machine Learning techniques to analyze patient diagnostic data and predict the likelihood of breast cancer. The trained model is integrated with a Flask-based web application that allows users to enter medical parameters and receive instant predictions.

---

## 🚀 Features

- Machine Learning-based cancer prediction
- User-friendly web interface
- Real-time prediction results
- Feature scaling using StandardScaler
- Flask REST API integration
- Fast and lightweight deployment
- Responsive frontend design

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning Libraries
- Scikit-learn
- Pandas
- NumPy

### Web Development
- Flask
- HTML
- CSS
- JavaScript

### Model Serialization
- Pickle

---

## 📂 Project Structure

```bash
Breast-Cancer-Detection/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── Breast_Cancer_Dataset_5000.xlsx
│
├── templates/
│   └── index.html
│
├── static/
│   ├── styles.css
│   ├── script.js
│   └── images/
│
├── README.md
└── requirements.txt
```

---

## 📊 Dataset Information

The dataset contains diagnostic measurements used for breast cancer classification.

### Dataset Statistics

| Attribute | Value |
|------------|---------|
| Total Samples | 5000 |
| Features | 30 |
| Target Classes | 2 |
| Benign Cases | 3120 |
| Malignant Cases | 1880 |

### Target Labels

| Label | Meaning |
|---------|---------|
| 0 | Benign |
| 1 | Malignant |

---

## 🧠 Machine Learning Workflow

### 1. Data Collection
Breast cancer diagnostic dataset collected and prepared for training.

### 2. Data Preprocessing
- Missing value handling
- Feature selection
- Data normalization
- Feature scaling using StandardScaler

### 3. Model Training
The dataset is used to train a machine learning classification model capable of distinguishing between benign and malignant tumors.

### 4. Model Serialization
The trained model and scaler are saved using Pickle for deployment.

### 5. Deployment
The trained model is integrated into a Flask web application for real-time predictions.

---

## 🔄 System Workflow

```text
User Input
     │
     ▼
Frontend Form
     │
     ▼
Flask Backend
     │
     ▼
Feature Scaling
     │
     ▼
Machine Learning Model
     │
     ▼
Prediction Result
     │
     ▼
Display Output
```

---

## 📷 Application Screenshots

### Home Page


```markdown
![Home Page](screenshots/home.png)
```

### Prediction Result

```markdown
![Prediction](screenshots/result.png)
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/SatishSwami/breast-cancer-detection_CI_Project.git
```

### Navigate to Project Directory

```bash
cd breast-cancer-detection_CI_Project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🌐 Access Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 📈 Prediction Output

The model predicts one of the following:

### 🟢 Benign
No indication of cancerous growth.

### 🔴 Malignant
Potential indication of breast cancer. Further medical examination is recommended.

---

## 🎯 Future Enhancements

- Deep Learning implementation
- Explainable AI (XAI)
- Cloud deployment
- Medical report generation
- PDF prediction reports
- Patient record management
- Mobile application integration
- Model performance dashboard

---

## 💡 Learning Outcomes

Through this project, the following concepts were implemented:

- Machine Learning Classification
- Data Preprocessing
- Feature Scaling
- Model Deployment
- Flask Development
- Frontend-Backend Integration
- API Development
- Model Serialization

---

## 👨‍💻 Author

**Satish Swami**

Electronics & Telecommunication Engineering  
MIT Academy of Engineering (MITAOE)

GitHub: https://github.com/SatishSwami

---

## 📜 License

This project is developed for educational and research purposes.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub!
