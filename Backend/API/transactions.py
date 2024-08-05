
def process_transaction(data):
    sender = data.get('sender')
    receiver = data.get('receiver')
    amount = data.get('amount')
    
    if not sender or not receiver or not amount:
        return 'Invalid transaction data'

    # Placeholder for actual transaction logic
    if amount <= 0:
        return 'Invalid transaction amount'

    # Assuming transaction is successful
    return 'Transaction successful'

def get_transaction_history(token):
    # Placeholder for retrieving transaction history
    # This should interact with the database to fetch actual data
    return [
        {'date': '2024-08-01', 'type': 'debit', 'amount': 100, 'status': 'completed'},
        {'date': '2024-08-02', 'type': 'credit', 'amount': 200, 'status': 'completed'},
    ]
