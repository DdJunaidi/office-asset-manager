import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- DATABASE LOGIC ---

def get_db_connection():
    """
    Connects to the SQLite database file.
    Think of this as opening the 'filing cabinet' where your data is kept.
    """
    conn = sqlite3.connect('assets.db')
    # This allows us to access data by column names like 'name' instead of just index numbers
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Initializes the database.
    This runs once when the app starts. If assets.db doesn't exist, it creates it.
    We added 'quantity' here to track how many items we have.
    """
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            quantity INTEGER DEFAULT 1,
            status TEXT DEFAULT 'In Use'
        )
    ''')
    conn.commit()
    conn.close()

# Start the database setup immediately
init_db()

# --- WEB ROUTES (The URLs you visit) ---

@app.route('/')
def index():
    """
    The Home Page.
    1. Opens database connection.
    2. Grabs every row from the 'assets' table.
    3. Sends that data to the index.html file to be displayed.
    """
    conn = get_db_connection()
    assets = conn.execute('SELECT * FROM assets').fetchall()
    conn.close()
    return render_template('index.html', assets=assets)

@app.route('/add', methods=('POST',))
def add_asset():
    """
    Triggered when you click 'Add Asset'.
    It takes the text from the inputs and 'INSERTs' a new row into the database.
    """
    # 'request.form' gets the data from the <input> tags in HTML
    name = request.form['name']
    category = request.form['category']
    quantity = request.form['quantity']
    
    if name and category:
        conn = get_db_connection()
        # The '?' are placeholders to prevent SQL Injection (a security best practice)
        conn.execute('INSERT INTO assets (name, category, quantity) VALUES (?, ?, ?)',
                     (name, category, quantity))
        conn.commit()
        conn.close()
    
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=('POST',))
def edit_asset(id):
    """
    Triggered when you 'Save Changes' in the Edit Modal.
    It finds the specific asset by its 'id' and 'UPDATEs' its values.
    """
    new_status = request.form['status']
    new_qty = request.form['quantity']
    
    conn = get_db_connection()
    conn.execute('UPDATE assets SET status = ?, quantity = ? WHERE id = ?',
                 (new_status, new_qty, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_asset(id):
    """
    Triggered when you click 'Delete'.
    Removes the row entirely from the database.
    """
    conn = get_db_connection()
    conn.execute('DELETE FROM assets WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # debug=True means the server restarts every time you save a file
    app.run(debug=True)