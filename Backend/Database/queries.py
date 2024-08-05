
from sqlalchemy.orm import Session
from models import User, Wallet, Transaction, QuantumTransaction

def get_user_wallet(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        return user.wallet
    return None

def update_wallet_balance(username, new_balance):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user and user.wallet:
        user.wallet.balance = new_balance
        session.commit()
    session.close()

def create_new_wallet(username):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        wallet = Wallet(user=user)
        session.add(wallet)
        session.commit()
        session.refresh(wallet)
        session.close()
        return wallet
    return None

def log_transaction(username, transaction_type, amount):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        transaction = Transaction(
            sender_id=user.id if transaction_type == 'withdraw' else None,
            receiver_id=user.id if transaction_type == 'deposit' else None,
            amount=amount,
            status='completed'
        )
        session.add(transaction)
        session.commit()
    session.close()

def store_phase_transaction(username, recipient_public_key, encrypted_symmetric_key, iv, encrypted_message):
    session = Session()
    user = session.query(User).filter_by(username=username).first()
    if user:
        transaction = QuantumTransaction(
            sender_id=user.id,
            recipient_public_key=recipient_public_key,
            encrypted_symmetric_key=encrypted_symmetric_key.hex(),
            iv=iv.hex(),
            encrypted_message=encrypted_message.hex()
        )
        session.add(transaction)
        session.commit()
        session.refresh(transaction)
        transaction_id = transaction.id
        session.close()
        return transaction_id
    return None

def retrieve_phase_transaction(transaction_id):
    session = Session()
    transaction = session.query(QuantumTransaction).filter_by(id=transaction_id).first()
    session.close()
    if transaction:
        return {
            'encrypted_symmetric_key': bytes.fromhex(transaction.encrypted_symmetric_key),
            'iv': bytes.fromhex(transaction.iv),
            'encrypted_message': bytes.fromhex(transaction.encrypted_message)
        }
    return None
