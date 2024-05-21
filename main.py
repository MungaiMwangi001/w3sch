from io import BytesIO
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy


#create a database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Upload(db.model):
    id=db.Column(db.Integer,primary_key=True)
    filename = db.Column(db.String(50))
    data = db.column(db.LargeBinary)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method =='POST':
        file = request.files['file']
        upload = Upload(filename=file.filename,data=file.read())
        db.Session.add(upload)
        db.session.commit()
        return 'File has been  uploaded'
    return render_template('index.html')