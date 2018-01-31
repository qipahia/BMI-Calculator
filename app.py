from flask import Flask, render_template, request
from models.user import User
from common.database import Database

app=Flask(__name__)

@app.before_first_request
def initialize_database():
    Database.initialize()

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
  
        new_user = User("Aaron Gonzalez", 170,60)
        new_user.save_to_mongo()
       
        user = User.find_by_id('0ff4a6d4e2ac4555adfa149d0c201241')
	
        if user is not None:
        
            height = user.height
            weight = user.weight
            bmi_retrieved = ((weight/height)/height)*10000
    
            return render_template("index.html",bmi=result, height=height,weight=weight,bmi_retrieved=bmi_retrieved)

        else:
            return render_template("index.html",bmi=result)

if __name__=='__main__':
    app.run()
