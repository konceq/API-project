from flask import Flask,render_template,request
import random
import api

app = Flask(__name__)

def getRest(search):
    restaurants = api.locu_search(search)
    x = random.randint(0, len(restaurants))
    answer = restaurants[x]
    return answer

@app.route("/", methods=['POST','GET'])
def index():
    if request.method=="POST":
        #print("hi")
        if request.form.get("search") != None:
            search = request.form.get("search")
            answer = getRest(search)
            words = answer.split(" ")
            y = 0
            while (api.tracks_search(words[y]) == None):
                y = y +1
                if y == len(words):
                    y = 0
                    answer = getRest(search)
                    words = answer.split(" ")
            values = api.tracks_search(words[y])
            return render_template("search.html", answer = answer, ID = values[0], Title = values[1], User = values[2])
        
    return render_template("search.html")

@app.route("/results")
def layout():
        return render_template("layout.html")

if __name__ == "__main__":
        app.debug=True
        app.run()

