from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/order")
def order():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_order():
    email = request.form.get("email")
    order = request.form.get("order")

    print("Email:", email)
    print("Order:", order)

    save_order(email, order)

    return render_template("submit.html")
@app.route('/')
def home():
    return render_template('home.html')

def save_order(email, order):
    conn = sqlite3.connect("orders.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            order_text TEXT
        )
    """)
    cur.execute("INSERT INTO orders (email, order_text) VALUES (?, ?)", (email, order))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True)

