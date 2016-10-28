from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

postList = [{"title": "The first", "content" : "blaljisjdfoiajsdf", "id":"123"}, {"title": "The Second", "content" : "yes", "id":"2a4"}]

@app.route("/")
@app.route("/home/")
def home():
    return render_template("index.html")
    #default route
    #center of it all
@app.route("/posts/")
def posts():
    return render_template("posts.html", postList = postList)

@app.route("/create/")
def create():
    return render_template("create.html")

@app.route("/newpost/", methods=["GET", "POST"])
def addPost():
    if request.method == "POST":
        print("adfjoasdf")
     
        t =request.form.get("postTitle")
        c =request.form.get("postContent")
        print (t)
       
        postList.append({"title": t, "content": c, "id": "333"})
        print("done")
        return "Cake"
    else:
        return "error"


@app.route("/posts/<postID>")
def show(postID):
    
    for p in postList:
        print(postID)
        print(p["id"])
        if p["id"] == postID:
            print("found")         
            title = str(p["title"])
            print(title)
            content = p["content"]
            tid = p["id"]
            post = [{"title":title, "content": content, "id": tid}]
            #return render_template(posts.html,post=post)
            return render_template("posts.html", postList=post)
        
        
    return page_not_found(postID)





@app.errorhandler(404)
def page_not_found(e):
    #official flask documentation
    err ="%s Not Found" % e
    return render_template('404.html',err=err), 404

if __name__ == "__main__":
    app.run(debug=True)
