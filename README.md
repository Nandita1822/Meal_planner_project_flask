# 🍽️ Meal Tracker - Health Nutrition & Planner App

A simple yet expandable web application to help users manage meals, calculate nutrition, and plan healthy eating habits. Built using **Flask** and **MySQL**.

---

## 🌟 About the Project

The **Meal Management & Nutrition Tracker** is a web-based full-stack application designed to help users organize their meals and monitor their nutritional intake.

The application allows users to add, view, update, and delete meal information, and to create customized meal plans by selecting multiple meals. It automatically calculates the combined nutritional values of the selected meals.

This project demonstrates practical implementation of **Python, Flask, MySQL, CRUD operations, SQL queries, server-side rendering, and full-stack web development**.

---

## ✨ Features

### 🔐 User Authentication
- 📝 User registration
- 🔑 User login

### 🍱 Meal Management
- ➕ Add new meals
- 👀 View complete meal details
- ✏️ Edit existing meals
- 🗑️ Delete meals
- 📋 Display all available meals
- 🔍 Filter meals by category or search by name

### 🥗 Nutrition Tracking
Track important nutritional information for every meal:
- 🔥 Calories
- 💪 Protein
- 🌾 Carbohydrates
- 🥑 Fat

### 📅 Meal Planning
- ✅ Select multiple meals
- 🧮 Automatically calculate total nutrition
- 📊 View combined calories, protein, carbohydrates, and fat
- 🍽️ Create customized meal plans

### 🗄️ Database Integration
- MySQL database integration
- Structured storage of meal information
- SQL queries for retrieving and modifying data

### 🎨 User Interface
- Responsive and intuitive UI using HTML/CSS + Jinja templating
- ⚡ Flash alerts for instant feedback (e.g., missing fields, successful updates)

---

## 🛠️ Tech Stack

### 🎨 Frontend
- HTML5
- CSS3
- Jinja2 Templating

### ⚙️ Backend
- 🐍 Python
- 🌐 Flask

### 🗄️ Database
- MySQL
- MySQL Connector/Python

### 🔧 Tools
- Git
- GitHub
- VS Code

---

## 📁 Project Structure

Meal_planner_project_flask/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── add_meal.html
│   ├── edit_meal.html
│   ├── view_meal.html
│   └── meal_plan.html
│
└── testing/
    ├── test_cases.md
    └── bug_report.md
```

---
## 🧪 Testing

Manual functional testing was performed on the live application.

- 📋 Test cases: [testing/test_cases.md](testing/test_cases.md)
- 🐞 Bug reports: [testing/bug_report.md](testing/bug_report.md)
  
--------

## ⚙️ Setup & Installation

1. 📥 Clone the repository
```bash
   git clone https://github.com/Nandita1822/Meal_planner_project_flask.git
   cd Meal_planner_project_flask
```
2. 📦 Install dependencies
```bash
   pip install -r requirements.txt
```
3. 🗄️ Create a MySQL database and update the database credentials in `app.py`
4. ▶️ Run the application
```bash
   python app.py
```
5. 🌐 Open `http://127.0.0.1:5000` in your browser

---

## 🌐 Live Demo

🚀 **Try the application online:**

👉 [Meal Management & Nutrition Tracker](https://nandita2205.pythonanywhere.com/register)
