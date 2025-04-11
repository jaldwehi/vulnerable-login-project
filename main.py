from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ⚠️ Vulnerable SQL query (no input validation)
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            message = 'Login Successful ✅'
        else:
            message = 'Login Failed ❌'

    return render_template('login.html', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
