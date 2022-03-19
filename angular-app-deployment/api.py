from functools import wraps
from os import abort
from tabnanny import check
import traceback
from flask import Blueprint, request
import json


from firebase_admin import firestore,auth

todo_item = Blueprint('todo_item', __name__)

db = firestore.client()

def checkToken(f):
    @wraps(f)
    def decorated_function(*args,**kws):
        if not 'Authorization' in request.headers:
            abort(401,{'message':'Unauthorized caller'})
        user=None
        try:
            data = request.headers['Authorization']
            header_token = str(data)
            token = header_token.split(" ")[-1]
            user = auth.verify_id_token(token)
            kws['uid'] = user['uid']
            kws['email'] = user['email']
        except Exception:
            traceback.print_exc()
            abort(401)
        return f(*args, **kws)
    return decorated_function


@todo_item.route('/item', methods=["POST"])
@checkToken
def add_todo_item(*args,**kws):
    data =request.json
    #print(data)
    docRef = db.collection(kws['email']).document()
    docRef.set(data)
    return json.dumps(
        {
            "status":"ok"
        }
    )
@todo_item.route('/list',methods=["POST"])
@checkToken
def display(*args,**kws):
    data = request.json
    docs = db.collection(kws['email']).get()
    resp = [doc.to_dict() for doc in docs]
    di = {"resp":resp}
    
    return json.dumps(di)
@todo_item.route("/delete",methods=["POST"])
@checkToken
def deleteTodo(*args,**kws):
    data = request.json

    docRef = db.collection(kws['email']).where(u'time',u'==',data['time']).get()
    for d in docRef:
        key = d.id
        db.collection(kws['email']).document(key).delete()
    return json.dumps({"status":"ok"})
@todo_item.route('/update',methods=["POST"])
@checkToken
def update(*args,**kws):
    data =request.json
    docs = db.collection(kws['email']).where(u'time',u'==',data['time']).get()
    for doc in docs:
        key = doc.id
        db.collection(kws['email']).document(key).update({'time':data['newtime'],'title':data['title']})
    return json.dumps({"status":"ok"})



