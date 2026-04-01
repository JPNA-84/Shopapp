from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def get_db():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'rootpass'),
        database=os.environ.get('DB_NAME', 'shopdb')
    )

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            db.commit()
            cursor.close()
            db.close()
            return redirect(url_for('login'))
        except Exception as e:
            error = "Username already exists."
    return render_template('signup.html', error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        db.close()
        if user:
            session['user'] = username
            return redirect(url_for('search'))
        else:
            error = "Invalid credentials."
    return render_template('login.html', error=error)

@app.route('/search')
def search():
    if 'user' not in session:
        return redirect(url_for('login'))
    query = request.args.get('q', '')
    products = []
    if query:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT id, name, description FROM products WHERE name LIKE %s OR description LIKE %s",
            (f'%{query}%', f'%{query}%')
        )
        products = cursor.fetchall()
        cursor.close()
        db.close()
    return render_template('search.html', products=products, query=query, user=session['user'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
