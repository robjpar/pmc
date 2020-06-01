from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sand_email import send_email
from sqlalchemy import func
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/height_collector'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class Data(db.Model):  # Data - table
    __tablemane__ = 'data'
    id = db.Column(db.Integer, primary_key=True)  # is - column
    email = db.Column(db.String(120), unique=True)  # emil - column
    height = db.Column(db.Integer)  # height - column

    def __init__(self, email, height):
        self.email = email
        self.height = height
# db.create_all() # run from a Python Shell


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']

        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height)
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count, simulate=True)
            return render_template('success.html')

        return render_template('index.html', text='Seems like we\'ve got something from that email already')


if __name__ == '__main__':
    app.debug = True
    app.run()
