from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/', methods= ['POST', 'GET'])

def welcome():

    result= 100000
    if request.method=='POST' and 'height' in request.form:
        u_height= int(request.form.get('height'))

    if request.method == 'POST' and 'weight' in request.form:
        u_weight=int(request.form.get('weight'))

    if request.method == 'POST':
        result=((u_weight/u_height)/u_height)*10000

    if result==100000:
        return render_template("index.html", bmi = 0)
    else:
        return render_template("index.html", bmi = result)


app.run()
