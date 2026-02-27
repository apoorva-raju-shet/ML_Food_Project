# 🍽️ ML Food Nutrition Analyzer

A Machine Learning based web application that predicts and displays nutritional information of food items using Flask and MongoDB.

---

## 📌 Project Overview

The ML Food Nutrition Analyzer is a web-based application that allows users to enter a food name and retrieve its nutritional details such as:

- Calories
- Protein
- Carbohydrates
- Fiber
- Sugar
- Potassium

The system fetches data from a MongoDB database and processes it using a machine learning model integrated with Flask.

---

## 🚀 Features

- 🔍 Search food items by name
- 📊 Display detailed nutrition information
- 🧠 Machine Learning model integration
- 🗄️ MongoDB database connectivity
- 🌐 Flask-based web interface

---

## 🛠️ Tech Stack

- Python
- Flask
- MongoDB
- PyMongo
- HTML
- Machine Learning

---

## 📂 Project Structure
ML_Food_Project/
│
├── app.py # Main Flask application
├── config.py # Database configuration
├── ml_model.py # Machine learning logic
├── requirements.txt # Required dependencies
├── dataset/ # Food dataset
├── templates/
│ └── index.html # Frontend template

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ML_Food_Project.git
cd ML_Food_Project
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the application
python app.py

Then open in browser:

http://127.0.0.1:5000/
📸 Sample Output

Users can enter a food name and receive structured nutritional information dynamically from the database.

📈 Future Improvements

Add user authentication

Improve UI design

Deploy on cloud (Render / Heroku)

Add more food datasets

Implement advanced ML predictions

👩‍💻 Author

Apoorva R Shet
CSE Student
Passionate about Machine Learning & Web Development

---
