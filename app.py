from flask import Flask, redirect, render_template, request, url_for, flash
import os
import mysql.connector
from dotenv import load_dotenv
import bcrypt

load_dotenv()

app = Flask(__name__)

# db-kobling
def db_connect():
    # kobler til db med info fra .env
    return mysql.connector.connect(
        database=os.environ.get("DB_NAME"),
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        port="3306"
    )

spk_db = db_connect()
cursor = spk_db.cursor()

def create_tables():
    cursor.execute("CREATE TABLE `user` (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL UNIQUE, email VARCHAR(255) NOT NULL, password VARCHAR(255))")
    spk_db.commit()

    
@app.route("/registrer", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        epost = request.form['email']
        # kode fra geeksforgeeks.org for hashing med bcrypt
        password = (request.form['password'])
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(bytes, salt)

        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s, %s)", 
                       (username, epost, password_hash, 'bruker'))
        spk_db.commit()
        cursor.close()
        spk_db.close()
        
        flash("User registered!", "success")
        return redirect(url_for("login"))

    return render_template("registrer.html")