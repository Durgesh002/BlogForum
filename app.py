from flask import *
import sqlite3

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/BlogForum'
# db = SQLAlchemy(app)

# class Contacts(db.Model):
#     # sno,name,email,phone_num,msg,date
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(20),  nullable=False)
#     phone_num = db.Column(db.String(12),  nullable=False)
#     msg = db.Column(db.String(120),  nullable=False)
#     date = db.Column(db.String(12), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods = ['POST', 'GET'])
def contact():
    msg = "msg"
    if request.method=='POST':
        try:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]
            with sqlite3.connect("contact.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Contact (name, email, phone, message) values (?,?,?,?)", (name, email, phone, message))
                con.commit()
                msg = "Contact added successfully"
        except:
            con.rollback()
            msg = "We cannot add contact"
        
    return render_template('contact.html')
    con.close()

@app.route('/post')
def post():
    return render_template('post.html')

if __name__=="__main__":
    app.run(debug=True)