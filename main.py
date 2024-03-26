from flask import Flask, render_template, request, redirect, jsonify
#from open import determineFood
import os
import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

imageURL = ""

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
  os.makedirs(UPLOAD_FOLDER)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/signin')
def signin():
  return render_template('signin.html')


@app.route('/search')
def search():
  return render_template('search.html')


@app.route('/foodName', methods=['POST'])
def getName():
  image = request.get_json()["foodName"]
  print(image)
  return render_template('search.html')


@app.route('/upload', methods=['POST'])
def upload_file():
  if request.method == 'POST':
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    print("File Uploaded Successfully")
  return redirect('/search')


@app.route('/download', methods=['POST'])
def parse():
  image = request.get_json()["image"]
  imageURL = image
  return render_template('search.html')

@app.route('/registering', methods=['GET', 'POST'])
def registering():
  print(request.method)
  if request.method == 'POST':
    print("registering")
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    print(email, password)
    try:
      user = auth.create_user(email=email, password=password)
      print(user)

    except Exception as e:
      print(e)
      return redirect('/register')
  else:
    print("Pooo")
  return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.get_json()["email"]
    password = request.get_json()["password"]
    print(email, password)
    try:
      user = auth.get_user_by_email(email)
      print(user)
      return render_template('search.html')
    except Exception as e:
      print(e)
      return render_template('search.html')
  return render_template('search.html')

@app.route('/register')
def register():
  return render_template('register.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
