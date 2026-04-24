from flask import Flask, render_template, request
import pandas as pd
from preprocess import preprocess
from train_model import train_model
from predict import predict

app = Flask(__name__)

# Load dataset and train model once
df = pd.read_excel("../Subtiq_AI_dataset.xlsx")
df = preprocess(df)
model = train_model(df)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        try:
            input_data = [
                float(request.form["ALT"]),
                float(request.form["GGT"]),
                float(request.form["Glucose"]),
                float(request.form["Creatine"]),
                int(request.form["THC"]),
                int(request.form["Cocaine"]),
                int(request.form["Opioid"]),
                float(request.form["pH"]),
                int(request.form["Attendance"]),
                int(request.form["Marks"]),
                int(request.form["Assignment"]),
                int(request.form["Leave"]),
                int(request.form["Mood"]),
                int(request.form["Peer"]),
                int(request.form["Discipline"]),
                int(request.form["Counsel"]),
                int(request.form["Social"]),
                int(request.form["Gaming"])
            ]

            result = predict(model, input_data)

        except:
            result = "Invalid input"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
