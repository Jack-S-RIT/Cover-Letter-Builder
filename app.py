from flask import Flask, redirect, render_template, request, url_for

from clb_api import generate_default_cover_letter_response, summarize_resume
app = Flask(__name__)



@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        # position = request.form["position"]
        # company = request.form["company"]
        resume = request.form["resume"]
        summary = summarize_resume(resume)
        # response = generate_default_cover_letter_response(position, company)
        return redirect(url_for("index", result=summary.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
