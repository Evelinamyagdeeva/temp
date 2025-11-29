# main.py
from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route("/")
def home():
    return render_template("index.html")

# Ещё одна страница для примера
@app.route("/about")
def about():
    return "<h1>О нас</h1><p>Это заглушка сайта на Flask.</p>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
