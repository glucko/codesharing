from flask import render_template, request, redirect, url_for, flash, Flask
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eriy02935234ohpjhdskvhxc070621234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.UnicodeText(), nullable=False)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts = posts)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        content = request.form['content']

        if content == "":
            flash("Please enter content")
        
        post = Post(content=content)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/delete', methods=['POST'])
def delete():
    Post.query.delete()
    db.session.commit()
    return "Deleted Successfully", 200