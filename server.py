from flask import *
from module.database2 import Database
import sqlite3,hashlib,os
from werkzeug.utils import secure_filename
import datetime

app=Flask(__name__)
app.secret_key='random string'
UPLOAD_FOLDER='static/uploads'
ALLOWED_EXTENSIONS=set(['jpeg','jpg','png','gif'])
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


db=Database()

@app.route('/')
def web2():
    return render_template('index.html')
@app.route('/login/')
def login():
    return render_template('login.html')
@app.route('/checkout/')
def checkout():
    return render_template('checkout.html')
@app.route('/signup/')
def signup():
    return  render_template('signup.html')
@app.route('/store/')
def store():
    return render_template('Store.html')
@app.route('/hindi/')
def hindi():
    return render_template('docshindi.html')
@app.route('/register',methods=['Post'])
def register():
    if request.method== 'POST':
        if db.insert(request.form):
            flash("product is added")
        else:
            flash("not added")
        return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/success',methods=['Post'])
def success():
    if request.method== 'POST':
        if db.match(request.form):
            return render_template('index2.html')
        else:
            return render_template('signup.html')
    else:
        return render_template('index.html')


def page_not_found(error):
    return render_template('error.html')
if __name__=='__main__':
    app.run(debug=True,port=9091,host="0.0.0.0")

