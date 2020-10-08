from flask import Flask,render_template,request,redirect,url_for,flash,abort,session,jsonify
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
# This allows us to securly send messgaes back and forth to the user so that they can't see this info
app.secret_key='hajaljhaksxakusyxajxuaydcxka'
@app.route("/")
def home():
    return render_template("home.html",codes=session.keys())#name="Harsh" if to pass a variable from here to page

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
            # flash for flask a way to display message as you move on to new web pages
            flash('That short code is already been taken. Please enter some other.')
            return redirect(url_for('home'))
        # Check wheather URL or string
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']  ## from HTML (name)
            full_name=request.form['code']+ secure_filename(f.filename)
            f.save('/home/harsh/Flask/url-shortner/static/user_files/'+full_name)
            urls[request.form['code']] = {'file':full_name}        
        #urls[request.form['code']] = {'url':request.form['url']}
        
        
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file) ##saving to json
            ##cookies for previous data
            session[request.form['code']] = True
        return render_template("your_url.html",code=request.form['code'])#,name="Harsh")
    else :
        return redirect(url_for('home'))

@app.route('/<string:code>')
### entering shortened url and going to actual
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls=json.load(urls_file)
            if code in urls.keys():
                ## checking key if file or url through iteration
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    ## Serving static file in Flask
                    return redirect(url_for('static',filename='user_files/'+urls[code]['file']))
    return abort(404)
## If some enter garbage route
@app.errorhandler(404)
def page_not_found(error):
    return render_template('no_page.html'),404

## Route for API
@app.route('/api')
def session_api():
    ## returning all the short code to json file format
    return jsonify(list(session.keys()))