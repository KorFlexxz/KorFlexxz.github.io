from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Kachalka.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Item(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.Text, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    des = db.Column(db.Text, nullable=True)
    def __repr__(self):
        return  self.title





@app.route('/')
def index():
    items = Item.query.order_by(Item.link).all()

    return render_template("index.html", data = items)

@app.route('/about')
def about():
   return render_template("about.html")

@app.route('/create.html', methods=['POST','GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        des = request.form['des']

        item = Item(title=title, link=link, des=des)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')

        except:

            return 'ошибка'
    else:

        return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)