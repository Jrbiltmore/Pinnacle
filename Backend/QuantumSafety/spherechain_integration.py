
import logging
from spherechain import SpherechainClient
from auth import decode_token

logging.basicConfig(level=logging.INFO)

SPHERECHAIN_API_KEY = 'your-spherechain-api-key'

class SpherechainIntegrationError(Exception):
    pass

spherechain_client = SpherechainClient(api_key=SPHERECHAIN_API_KEY)

def initiate_spherechain_transaction(token, recipient, amount, data):
    try:
        username = decode_token(token)
        if not username:
            raise SpherechainIntegrationError('Unauthorized access')

        transaction_id = spherechain_client.create_transaction(
            sender=username,
            recipient=recipient,
            amount=amount,
            data=data
        )

        logging.info(f"Spherechain transaction initiated by {username} with ID: {transaction_id}")
        return {'transaction_id': transaction_id}
    except SpherechainIntegrationError as e:
        logging.error(f"Error initiating Spherechain transaction: {str(e)}")
        return {'error': str(e)}

def get_spherechain_transaction_status(transaction_id):
    try:
        status = spherechain_client.get_transaction_status(transaction_id)
        logging.info(f"Retrieved Spherechain transaction status for ID: {transaction_id}")
        return {'status': status}
    except Exception as e:
        logging.error(f"Error retrieving Spherechain transaction status: {str(e)}")
        raise SpherechainIntegrationError(f"Failed to get transaction status: {str(e)}")
