from flask import Flask,render_template,request,redirect,url_for
import json
import os.path

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")#name="Harsh" if to pass a variable from here to page

@app.route('/your-url',methods=['GET','POST'])
def your_url():
    # Check if method is POST then write other wise redirect it to Home page
    if request.method == 'POST':
        ##code saving that user passed to a json
        urls={}
        ## Checking for value already exists!!
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
            #taking content inside of this file and put into urls{}
                urls=json.load(urls_file)
        # if short name or code is present redirecting to home page
        if request.form['code'] in urls.keys():
            return redirect(url_for('home'))
            

        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file) ##saving to json
        return render_template("your_url.html",code=request.form['code'])#,name="Harsh")
    else :
        return redirect(url_for('home'))
