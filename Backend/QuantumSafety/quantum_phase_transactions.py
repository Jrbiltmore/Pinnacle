
import logging
from quantum_encryption import encrypt_message, decrypt_message, generate_key_pair
from auth import decode_token
from database import store_phase_transaction, retrieve_phase_transaction

logging.basicConfig(level=logging.INFO)

class QuantumPhaseTransactionError(Exception):
    pass

def initiate_phase_transaction(token, recipient_public_key_pem, message):
    try:
        username = decode_token(token)
        if not username:
            raise QuantumPhaseTransactionError('Unauthorized access')

        encrypted_symmetric_key, iv, encrypted_message = encrypt_message(recipient_public_key_pem, message)
        transaction_id = store_phase_transaction(username, recipient_public_key_pem, encrypted_symmetric_key, iv, encrypted_message)

        logging.info(f"Phase transaction initiated by {username} with ID: {transaction_id}")
        return {'transaction_id': transaction_id}
    except QuantumPhaseTransactionError as e:
        logging.error(f"Error initiating phase transaction: {str(e)}")
        return {'error': str(e)}

def complete_phase_transaction(private_key_pem, transaction_id):
    try:
        transaction = retrieve_phase_transaction(transaction_id)
        if not transaction:
            raise QuantumPhaseTransactionError('Transaction not found')

        decrypted_message = decrypt_message(private_key_pem, transaction['encrypted_symmetric_key'], transaction['iv'], transaction['encrypted_message'])

        logging.info(f"Phase transaction completed with ID: {transaction_id}")
        return {'message': decrypted_message}
    except QuantumPhaseTransactionError as e:
        logging.error(f"Error completing phase transaction: {str(e)}")
        return {'error': str(e)}
