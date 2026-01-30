from flask import Flask, redirect, render_template, request, url_for, flash, session
import os
import mysql.connector
from dotenv import load_dotenv
import bcrypt

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY")

# db-kobling
def db_connect():
    # kobler til db med info fra .env
    return mysql.connector.connect(
        database=os.environ.get("DB_NAME"),
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        port=os.environ.get("DB_PORT")
    )

spk_db = db_connect()
cursor = spk_db.cursor()

def create_tables():
    # lager user-tabell
    # bør bruke backticks på navn user pga det er en ting i mysql fra før
    cursor.execute("CREATE TABLE `user` (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL UNIQUE, email VARCHAR(255) NOT NULL UNIQUE, password CHAR(60) NOT NULL, role VARCHAR(50))")
    # lager boardgame-tabell
    cursor.execute("CREATE TABLE boardgame (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, creator VARCHAR(255), publisher VARCHAR(255), description TEXT DEFAULT CHARSET=utf8mb4)")
    spk_db.commit()

# Route for hjemside
@app.route("/")
def index():
    return render_template(url_for("index"))

# Route for registrering
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        epost = request.form['email']
        # kode fra geeksforgeeks.org for hashing med bcrypt
        password = (request.form['password'])
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash_bytes = bcrypt.hashpw(password_bytes, salt)
        # siden jeg bruker CHAR(60) i DB må jeg omgjøre til tekststreng
        password_hash_str = password_hash_bytes.decode()

        cursor.execute("INSERT INTO user (username, email, password) VALUES (%s, %s, %s)", (username, epost, password_hash_str))
        spk_db.commit()
        cursor.close()
        spk_db.close()
        
        flash("User registered!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# Route for innlogging
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if not user:
            return render_template("login.html", error_message="Invalid username or password")
        
        db_password = user['password'].encode('utf-8')

        if user and bcrypt.checkpw(password, db_password):
            session['username'] = user['username']
            
            return render_template("login.html", login_message="You are now logged in!")

    return render_template("login.html")