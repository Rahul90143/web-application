from flask import Flask, render_template, request, url_for, Markup, jsonify,session
import pickle
from database import *
import hashlib
import re
from collections import defaultdict

app = Flask(__name__)
app.secret_key = "hello"
 
app.config['UPLOAD_FOLDER'] = 'static/uploads'
pickle_in = open('model_fakenews.pickle','rb')
pac = pickle.load(pickle_in)
tfid = open('tfid.pickle','rb')
tfidf_vectorizer = pickle.load(tfid)


def clean_text(text):
    # Regular expression to keep only alphanumeric characters and spaces
    cleaned_text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return cleaned_text
@app.route('/')
def home():
 	return render_template("index.html")
@app.route('/uh')
def uhome():
 	return render_template("uhome.html")
@app.route('/ah')
def ahome():
 	return render_template("ahome.html")
@app.route('/br')
def br():
 	return render_template("breg.html")
@app.route('/al')
def al():
 	return render_template("admin.html")
@app.route('/ar')
def ar():
 	return render_template("adminreg.html")
@app.route('/bl')
def bl():
 	return render_template("blogin.html")
@app.route('/uadd')
def addn():
 	return render_template("addnews.html")
@app.route('/log')
def log():
 	return render_template("index.html")
@app.route("/uv")
def VED2():
    data=view1(session['username'])
    print("done",data)
    return render_template("mynews.html",data=data)
@app.route("/av")
def VED3():
    data=view()
    print("done",data)
    return render_template("allnews.html",data=data)
@app.route("/afv")
def VED5():
    data=view()
    print("done",data)
    return render_template("fake.html",data=data)
@app.route("/sv")
def VED():
    data=view3(session['username'])
    print("done",data)
    return render_template("sharenews.html",data=data)
@app.route("/bregister",methods=['POST','GET'])
def signup():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        add=request.form['Location']
        ph=request.form['Phone no']
        status = user_reg(username,email,password,add,ph) 
        if status == 1:
            return render_template("blogin.html")
        else:
            return render_template("breg.html",m1="failed")        
    

@app.route("/blogin",methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        status = user_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1: 
            session['username'] = request.form['username']                                     
            return render_template("uhome.html", m1="sucess")
        else:
            return render_template("blogin.html", m1="Login Failed")


@app.route("/aregister",methods=['POST','GET'])
def asignup():
    if request.method=='POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        status = auser_reg(username,email,password) 
        if status == 1:
            return render_template("admin.html")
        else:
            return render_template("adminreg.html",m1="failed")        
    

@app.route("/alogin",methods=['POST','GET'])
def alogin():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        status = auser_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1: 
            session['username'] = request.form['username']                                     
            return render_template("ahome.html", m1="sucess")
        else:
            return render_template("admin.html", m1="Login Failed")

def generate_hashcode(news, title):
    combined_data = news + title
    hashcode = hashlib.sha256(combined_data.encode()).hexdigest()
    return hashcode

@app.route('/newscheck',methods=['POST','GET'])
def newscheck():
    NEWS=request.form['news']
    t=request.form['title']
    input_data = [NEWS.rstrip()]
    tfidf_test = tfidf_vectorizer.transform(input_data)
    # predicting the input
    y_pred = pac.predict(tfidf_test)
    name=session['username']
    NEWS=clean_text(NEWS)
    t=clean_text(t)
    addnewsr(name,t,NEWS,y_pred[0],generate_hashcode(NEWS,t))
    return render_template("addnews.html")

@app.route('/send',methods=['POST','GET'])
def send():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    param3 = request.args.get('param3')
    return render_template("send.html", param1=param1,param2=param2,param3=param3)
@app.route('/sent',methods=['POST','GET'])
def sent():
    se=session['username']
    s1=session['username']
    param1 =request.form['param1']
    param2 =request.form['param2']
    param3 = request.form['param3']
    r=request.form['uname']
    res=s(s1,param1,param2,param3,se,r)
    return render_template("uhome.html")

@app.route('/send2',methods=['POST','GET'])
def send2():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    param3 = request.args.get('param3')
    param4 = request.args.get('param4')
    return render_template("send2.html", param1=param1,param2=param2,param3=param3,param4=param4)
@app.route('/sent2',methods=['POST','GET'])
def sent2():
    se=session['username']
    s1=request.form['param4']
    param1 =request.form['param1']
    param2 =request.form['param2']
    param3 = request.form['param3']
    r=request.form['uname']
    print('done',s1)
    res=s(s1,param1,param2,param3,se,r)
    return render_template("uhome.html")
@app.route('/report',methods=['POST','GET'])
def report2():
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    data=report(param1)
        # Group `r` values by `s` keys
    grouped_data = defaultdict(list)
    for record in data:
        s = record[4]  # `s` value
        r = record[5]  # `r` value
        grouped_data[s].append(r)

    # Convert to regular dictionary to pass to the template
    grouped_data = dict(grouped_data)

    return render_template("report.html",param2=param2,grouped_data=grouped_data)

if __name__=='__main__':
    app.run(debug=True)
