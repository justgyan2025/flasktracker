from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from dotenv import load_dotenv
import os
import yfinance as yf

# Load environment variables
load_dotenv(dotenv_path=".env")

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')

# Firebase configuration for client-side
app.config.update({
    'FIREBASE_API_KEY': os.getenv('FIREBASE_API_KEY'),
    'FIREBASE_AUTH_DOMAIN': os.getenv('FIREBASE_AUTH_DOMAIN'),
    'FIREBASE_PROJECT_ID': os.getenv('FIREBASE_PROJECT_ID'),
    'FIREBASE_STORAGE_BUCKET': os.getenv('FIREBASE_STORAGE_BUCKET'),
    'FIREBASE_MESSAGING_SENDER_ID': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    'FIREBASE_APP_ID': os.getenv('FIREBASE_APP_ID')
})

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Username from form: {username}")
        print(f"Password from form: {password}")
        print(f"Username from .env: {USERNAME}")
        print(f"Password from .env: {PASSWORD}")
        print(f"Username from os.environ after load_dotenv: {os.environ.get('USERNAME')}")
        print(f"Password from os.environ after load_dotenv: {os.environ.get('PASSWORD')}")
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials', config=app.config)
    return render_template('login.html', config=app.config)

def login_required(f):
    def decorated_function(*args, **kwargs):
        if session.get('logged_in'):
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return decorated_function

@app.route('/')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard', config=app.config)

@app.route('/stocks')
def stocks():
    return render_template('stocks.html', active_page='stocks', config=app.config)

@app.route('/mutual-funds')
def mutual_funds():
    return render_template('mutual_funds.html', active_page='mutual_funds', config=app.config)

@app.route('/nps')
def nps():
    return render_template('nps.html', active_page='nps', config=app.config)

@app.route('/logout')
@login_required
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/get_stock_info')
def get_stock_info():
    try:
        symbol = request.args.get('symbol', '')
        # Add .NS suffix for NSE stocks
        if not symbol.endswith('.NS'):
            symbol = f"{symbol}.NS"
        
        stock = yf.Ticker(symbol)
        info = stock.info
        
        if 'regularMarketPrice' not in info:
            return jsonify({
                'error': 'Stock not found or not available'
            }), 404
            
        return jsonify({
            'name': info.get('longName', ''),
            'symbol': symbol,
            'currentPrice': info.get('regularMarketPrice', 0),
            'dayHigh': info.get('dayHigh', 0),
            'dayLow': info.get('dayLow', 0),
            'previousClose': info.get('previousClose', 0)
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
