from datetime import datetime
from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)  #initializing the flask app
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///wastemanagement.db"
app.config['SQLALCHEMY_TRACK_MODIFICATTIONS']=False
db=SQLAlchemy(app)





class WasteManagement(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
   

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

  
with app.app_context():
    db.create_all()    



@app.route("/")  #gives the home page
def home():
    return render_template('index2.html')



@app.route("/index",methods=['GET','POST'])  #gives the indexx page
def index():
    if request.method=='POST':
        title=request.form["title"]
        desc=request.form['desc']
        wastemanagement=WasteManagement(title=title,desc=desc)
        # todo=db.session.query(Todo).filter_by(title=title,desc=desc).first()
        db.session.add(wastemanagement)
        db.session.commit()
    allWaste=WasteManagement.query.all()
    return render_template('index.html',allWaste=allWaste)

@app.route("/products") 
def products():
    allWaste=WasteManagement.query.all()
    print(allWaste)
    return "Welcome to the products page"

@app.route("/delete/<int:sno>") 
def delete(sno):
    wastemanagement=WasteManagement.query.filter_by(sno=sno).first()
    db.session.delete(wastemanagement)
    db.session.commit()
    return redirect("/index")

@app.route("/update/<int:sno>",methods=['GET','POST']) 
def update(sno):
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        wastemanagement=WasteManagement.query.filter_by(sno=sno).first()
        wastemanagement.title=title
        wastemanagement.desc=desc
        db.session.add(wastemanagement)
        db.session.commit()
        return redirect("/index")
    wastemanagement=WasteManagement.query.filter_by(sno=sno).first()
    
    return render_template('update.html',wastemanagement=wastemanagement)

    




if __name__=="__main__":  #entry point of flask application 
    app.run(debug=True) #by debug=True we do not have to restart everytime when we make changes
    #use debug = true when you are debugging