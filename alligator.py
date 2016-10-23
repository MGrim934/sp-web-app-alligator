from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def hello():
    #using render_template to serve basic shell
    #Flask quickstart guide was helpful http://flask.pocoo.org/docs/0.11/quickstart/
    return render_template("index.html")

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/posts/")
def posts():
    myPosts = "Cake"
    return render_template("posts.html", post=myPosts)

@app.errorhandler(404)
def page_not_found(e):
    #official flask documentation
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
