from flask import Flask, redirect, render_template, request, url_for

from clb_api import generate_default_cover_letter_response
app = Flask(__name__)



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        position = request.form["position"]
        company = request.form["company"]
        response = generate_default_cover_letter_response(position, company)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
