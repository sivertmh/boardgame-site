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

def create_tables():
    
    conn = db_connect()
    cursor = conn.cursor()
    
    # lager user-tabell
    # bør bruke backticks på navn user pga det er en ting i mysql fra før
    cursor.execute("""
        CREATE TABLE `user` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            password CHAR(60) NOT NULL,
            role VARCHAR(50)
                       )""")
    # lager boardgame-tabell
    cursor.execute("""
        CREATE TABLE boardgame (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            year_published INT,
            creator VARCHAR(255),
            publisher VARCHAR(255),
            description TEXT CHARACTER SET utf8mb4
            )""")
    conn.commit()
    
try:
    create_tables()
    print("Tabeller ble laget!")
except:
    print("Tabeller ble ikke laget. (finnes kanskje fra før)")

# Route for hjemside
@app.route("/")
def index():
    
    conn = db_connect()
    cursor = conn.cursor()

    # henter info som skal vises på forside i en tuple
    cursor.execute("SELECT name, year_published, publisher FROM boardgame")
    bg_info = cursor.fetchall()
    
    return render_template("index.html", bg_info=bg_info)

# Route for registrering
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        conn = db_connect()
        cursor = conn.cursor()
        
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
        conn.commit()
        cursor.close()
        conn.close()
        
        flash("User registered!", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

# Route for registrering av brettspill
@app.route("/register_boardgame", methods=["GET", "POST"])
def register_boardgame():
    if request.method == "POST":
        bg_name = request.form['name']
        year = request.form['year']
        creator = request.form['creator']
        publisher = request.form['publisher']
        desc = request.form['description']
        
        conn = db_connect()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO boardgame (name, year_published, creator, publisher, description) VALUES (%s, %s, %s, %s, %s)", (bg_name, year, creator, publisher, desc))
        conn.commit()
        cursor.close()
        conn.close()
        
        flash("Boardgame registered!", "success")
        return redirect(url_for("register_boardgame"))
    return render_template("register_boardgame.html")

# Route for innlogging.
# Basert på kode fra tidligere oppgave.
# Bcrypt istedenfor Werkzeug.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        
        conn = db_connect()
        cursor = conn.cursor(dictionary=True)
        
        # henter brukernavn
        cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        # henter passord og gjør om til bytes
        db_password = user['password'].encode('utf-8')

        if user and bcrypt.checkpw(password, db_password):
            session['username'] = user['username']
            session['rolle'] = user['rolle']
            
            return render_template("login.html", login_message="You are now logged in!")
        else:
            return render_template("login.html", error_message="Invalid username or password")
    return render_template("login.html")