from flask import Flask,render_template,request
import random
import api

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if request.method=="POST":
        print("hi")
        if request.form.get("search") != None:
            search = request.form.get("search")
        restaurants = api.locu_search(search)
        x = random.randint(0, len(restaurants))
        answer = restaurants[x]
        return render_template("layout.html", answer = answer)
        
    return render_template("search.html")

@app.route("/results")
def layout():
        return render_template("layout.html")

if __name__ == "__main__":
        app.debug=True
        app.run()

