from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kowsalya:Kowsi@localhost:5432/test1'
app.debug = True
db = SQLAlchemy(app)


class Usertable(db.Model):
    __tablename__ = 'usertable'
    user_id = db.Column('user_id', db.Integer, primary_key=True)
    user_name = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(50),nullable=False)
    company_name = db.Column(db.String(200),nullable=False)
    phn_no = db.Column(db.Integer,nullable=False)
    status = db.Column(db.Boolean,default=1)

    def __init__(self,user_id, user_name,password, company_name, phn_no,status):
        self.user_id_id = user_id
        self.user_name = user_name
        self.password = password
        self.company_name = company_name
        self.phn_no = phn_no
        self.status=status


@app.route('/userentries',methods=['POST'])
def userent():
    data=request.get_json()
    #print(ipt)
    det=Usertable(user_id=data['user_id'],user_name=data['user_name'],password=data['password'],company_name=data['company_name'],phn_no=data['phn_no'],status=data['status'])
    db.session.add(det)
    db.session.commit()
    return("successfully created")
#db.create_all()
#db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
