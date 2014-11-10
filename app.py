from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
        return render_template("search.html", methods=["GET", "POST"])

@app.route("/results")
def search():
        return render_template("layout.html")

if __name__ == "__main__":
        app.debug=True
        app.run()

