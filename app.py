from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import mysql.connector

app = Flask(__name__)

#
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "12345",  
    "database": "meals_db"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route("/")
def index():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM meals ORDER BY id DESC")
    meals = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("index.html", meals=meals)


@app.route("/add", methods=["GET", "POST"])
def add_meal():
    if request.method == "POST":
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO meals (name, category, ingredients, calories, protein, carbs, fat, instructions, timestamp)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            request.form["name"],
            request.form["category"],
            request.form["ingredients"],
            int(request.form.get("calories", 0)),
            int(request.form.get("protein", 0)),
            int(request.form.get("carbs", 0)),
            int(request.form.get("fat", 0)),
            request.form.get("instructions", ""),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("index"))

    return render_template("add_meal.html")


@app.route("/view/<int:meal_id>")
def view_meal(meal_id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM meals WHERE id=%s", (meal_id,))
    meal = cur.fetchone()
    cur.close()
    conn.close()
    if meal:
        return render_template("view_meal.html", meal=meal)
    return redirect(url_for("index"))


@app.route("/edit/<int:meal_id>", methods=["GET", "POST"])
def edit_meal(meal_id):
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM meals WHERE id=%s", (meal_id,))
    meal = cur.fetchone()

    if not meal:
        cur.close()
        conn.close()
        return redirect(url_for("index"))

    if request.method == "POST":
        cur.execute("""
            UPDATE meals SET name=%s, category=%s, ingredients=%s,
            calories=%s, protein=%s, carbs=%s, fat=%s, instructions=%s
            WHERE id=%s
        """, (
            request.form["name"],
            request.form["category"],
            request.form["ingredients"],
            int(request.form.get("calories", 0)),
            int(request.form.get("protein", 0)),
            int(request.form.get("carbs", 0)),
            int(request.form.get("fat", 0)),
            request.form.get("instructions", ""),
            meal_id
        ))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("view_meal", meal_id=meal_id))

    cur.close()
    conn.close()
    return render_template("edit_meal.html", meal=meal)


@app.route("/delete/<int:meal_id>", methods=["POST"])
def delete_meal(meal_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM meals WHERE id=%s", (meal_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("index"))


@app.route("/plan", methods=["GET", "POST"])
def meal_plan():
    conn = get_db_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM meals ORDER BY id DESC")
    meals = cur.fetchall()

    selected_meals = []
    totals = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}

    if request.method == "POST":
        ids = request.form.getlist("meal_ids")
        format_strings = ','.join(['%s'] * len(ids))
        cur.execute(f"SELECT * FROM meals WHERE id IN ({format_strings})", tuple(ids))
        selected_meals = cur.fetchall()
        for m in selected_meals:
            totals["calories"] += m["calories"]
            totals["protein"] += m["protein"]
            totals["carbs"] += m["carbs"]
            totals["fat"] += m["fat"]

    cur.close()
    conn.close()
    return render_template("meal_plan.html", meals=meals, selected_meals=selected_meals, totals=totals)


if __name__ == "__main__":
    app.run(debug=True)
