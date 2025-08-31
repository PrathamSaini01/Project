import joblib
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    model_stuff = joblib.load("Model/model.pkl")   # 🔹 Make sure path is correct
    return render_template(
        "dashboard.html",
        mse=model_stuff["mse"],
        r2=model_stuff["r2"],
        scree=model_stuff["plots"]["scree"],
        scatter=model_stuff["plots"]["scatter"],
        predicted=model_stuff["plots"]["predicted"],
        residuals=model_stuff["plots"]["residuals"]
    )

if __name__ == "__main__":
    app.run(debug=True)
