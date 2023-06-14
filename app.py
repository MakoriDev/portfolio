from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__, static_folder='static')
app.config['STATIC_FOLDER'] = ['static', 'assets']
app.config['MONGO_URI'] = 'mongodb://localhost:27017/portfolio' 
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'message': request.form.get('message')
        }
        mongo.db.messages.insert_one(data)
        return 'Your Message is sent successfully!'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
