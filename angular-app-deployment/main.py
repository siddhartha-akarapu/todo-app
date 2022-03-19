from flask import Flask,Blueprint,render_template,send_from_directory
from flask_cors import CORS
import firebase_admin

firebase_admin.initialize_app()
from api import todo_item


app = Flask(__name__)
CORS(app)



todoapp = Blueprint('todoapp',__name__,template_folder='todo-list-app/dist/todo-list-app')
app.register_blueprint(todoapp)
app.register_blueprint(todo_item, url_prefix = "/api")

@app.route('/assets/<path:filename>')
def custom_static_for_assets(filename):
    return send_from_directory('todo-list-app/dist/todo-list-app/assets',filename)

@app.route('/<path:filename>')
def custom_static(filename):
    return send_from_directory('todo-list-app/dist/todo-list-app/',filename)

@app.route('/')
def index():
    return render_template("index.html")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)

