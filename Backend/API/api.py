
from flask import Flask, jsonify, request
from auth import authenticate_user
from transactions import process_transaction, get_transaction_history
from wallets import get_wallet_balance, create_wallet
from plaid_integration import get_financial_data

app = Flask(__name__)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if authenticate_user(username, password):
        return jsonify({'message': 'Login successful', 'token': 'your-jwt-token'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/wallet', methods=['GET'])
def wallet_balance():
    token = request.headers.get('Authorization')
    if not token or not authenticate_user(token):
        return jsonify({'message': 'Unauthorized'}), 401
    balance = get_wallet_balance(token)
    return jsonify({'balance': balance}), 200

@app.route('/api/wallet', methods=['POST'])
def create_user_wallet():
    token = request.headers.get('Authorization')
    if not token or not authenticate_user(token):
        return jsonify({'message': 'Unauthorized'}), 401
    wallet = create_wallet(token)
    return jsonify({'wallet': wallet}), 201

@app.route('/api/transactions', methods=['POST'])
def make_transaction():
    token = request.headers.get('Authorization')
    if not token or not authenticate_user(token):
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.json
    transaction_status = process_transaction(data)
    return jsonify({'status': transaction_status}), 200

@app.route('/api/transactions', methods=['GET'])
def transaction_history():
    token = request.headers.get('Authorization')
    if not token or not authenticate_user(token):
        return jsonify({'message': 'Unauthorized'}), 401
    history = get_transaction_history(token)
    return jsonify({'transactions': history}), 200

@app.route('/api/financial_data', methods=['GET'])
def financial_data():
    token = request.headers.get('Authorization')
    if not token or not authenticate_user(token):
        return jsonify({'message': 'Unauthorized'}), 401
    data = get_financial_data(token)
    return jsonify({'financial_data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
