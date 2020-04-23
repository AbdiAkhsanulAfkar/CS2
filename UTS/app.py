from flask_restful import Resource, Api
from flask import Flask, Response, json, jsonify, request, abort, render_template, flash, redirect, url_for,request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.secret_key = "Secret Key"
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/kampus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    NIM = db.Column(db.CHAR(10), unique=True, nullable = False)
    Nama = db.Column(db.CHAR(100), nullable = False)
    Alamat = db.Column(db.Text)


    def __init__(self, NIM, Nama, Alamat):
        self.NIM = NIM
        self.Nama = Nama
        self.Alamat = Alamat


@app.route('/')
def Index():
    all_data = Mahasiswa.query.all()

    return render_template("index.html", mahasiswa=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        NIM = request.form['NIM']
        Nama = request.form['Nama']
        Alamat = request.form['Alamat']

        mhs = Mahasiswa(NIM, Nama, Alamat)
        db.session.add(mhs)
        db.session.commit()

        flash("Berhasil Menambahkan Data")

        return redirect(url_for('Index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        data = Mahasiswa.query.get(request.form.get('id'))

        data.NIM = request.form['NIM']
        data.Nama = request.form['Nama']
        data.Alamat = request.form['Alamat']

        db.session.commit()
        flash("Employee Updated Successfully")

        return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    mhs = Mahasiswa.query.get(id)
    db.session.delete(mhs)
    db.session.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run()
