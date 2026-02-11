from flask import Flask, redirect, render_template, request, url_for, flash, session
import os
import mysql.connector
from dotenv import load_dotenv
import bcrypt

# Boilerplate-kode.
load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY")

# Db-kobling.
def db_connect():
    # Kobler til db med info fra Environment-fil.
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
    
    # Lager user-tabell.
    # Bruker backticks på tabellnavnet "user". Dette er pga at det er en ting i Mysql fra før.
    cursor.execute("""
        CREATE TABLE `user` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            password CHAR(60) NOT NULL,
            role VARCHAR(50)
                       )""")
    # Lager boardgame-tabell.
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

# Prøver å kjøre funksjon "create_tables".
try:
    create_tables()
    print("Tabeller ble laget!")
except:
    print("Tabeller ble ikke laget. (ignorer om de finnes fra før)")

# Route for hjemside.
@app.route("/")
def index():
    
    conn = db_connect()
    cursor = conn.cursor()

    # Henter info som skal vises på forside i en tuple.
    cursor.execute("SELECT name, year_published, publisher FROM boardgame")
    bg_info = cursor.fetchall()
    
    return render_template("index.html", bg_info=bg_info)

# Route for registrering.
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
        
        # Henter brukernavn.
        cursor.execute("SELECT * FROM user WHERE username=%s", (username,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        # Henter passord og gjør om til bytes.
        if user:
            db_password = user['password'].encode('utf-8')

        if bcrypt.checkpw(password, db_password):
            session['username'] = user['username']
            session['role_id'] = user['role_id']
            
            flash("You are now logged in!")
            return redirect(url_for("index"))
            
        else:
            flash("Invalid username or password")
            return redirect(url_for("login"))
    return render_template("login.html")

# Route for registrering av brettspill.
@app.route("/register_boardgame", methods=["GET", "POST"])
def register_boardgame():
    
    conn = db_connect()
    cursor = conn.cursor()
    
    # Fra "How to use Flask-Session in Python Flask". Se kilder.
    if not session.get("username") or not session.get("role_id"):
        flash("You must be logged in (as admin or editor) to access '/register_boardgame'.")
        return redirect(url_for("index"))
    
    # Kodesnutt er fikset/minimalisert ved hjelp av KI.
    # Roller: admin (1), editor (2), user (3).
    if session["role_id"] not in (1, 2):
        flash("Only admins and editors can access '/register_boardgame'.")
        return redirect(url_for("index"))
    
    if request.method == "POST":
        bg_name = request.form['name']
        year = request.form['year']
        creator = request.form['creator']
        publisher = request.form['publisher']
        desc = request.form['description']
        
        if not bg_name:
            flash("Name is required.")
            return redirect(url_for("register_boardgame"))
        
        cursor.execute("""INSERT INTO boardgame ( 
                            name, 
                            year_published, 
                            creator, 
                            publisher, 
                            description
                            ) VALUES (%s, %s, %s, %s, %s)""", (bg_name, year, creator, publisher, desc))
        
        flash("Boardgame registered!", "success")
        return redirect(url_for("register_boardgame"))
    
    conn.commit()
    cursor.close()
    conn.close()
    
    return render_template("register_boardgame.html")

# Route for å logge ut.
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
