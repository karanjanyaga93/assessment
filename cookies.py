from flask import Flask,redirect,make_response,render_template,request
app=Flask(_name_)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template(index.html')

@app.route('/setcookies',methods=['GET','POST'])
def setcookies():
    if request.method=='POST'
         name = request.form['name']
         resp = make_response(render_template('readcookies.html'))
         resp.set_cookie('username','tanzania')


         return resp


@app.route('/readcookies')
def readcookies():