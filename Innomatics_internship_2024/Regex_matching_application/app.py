from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home3.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    matches = re.findall(regex_pattern, test_string)
    return render_template("home3.html", matches=matches)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
