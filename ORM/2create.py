from flask import Flask,request,render_template
from models import *

app = Flask(__name__)
POSTGRES = {
    'user': 'postgres',
    'pw': 'rakib1602066',
    'db': 'mydatabase',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
#app.config["SQLALCHEMY_DATABASE_URL"]="postgresql://postgres:rakib1602066@localhost/mydatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        main()


