
import logging
from database import get_user_wallet, update_wallet_balance, create_new_wallet, log_transaction
from auth import decode_token
from events import trigger_event

logging.basicConfig(level=logging.INFO)

class WalletError(Exception):
    pass

async def get_wallet_balance(token):
    try:
        username = decode_token(token)
        if not username:
            raise WalletError('Unauthorized access')

        wallet = await get_user_wallet(username)
        if not wallet:
            raise WalletError('Wallet not found')

        logging.info(f"Retrieved balance for user: {username}")
        return {'balance': wallet['balance']}
    except WalletError as e:
        logging.error(f"Error retrieving wallet balance: {str(e)}")
        return {'error': str(e)}

async def create_wallet(token):
    try:
        username = decode_token(token)
        if not username:
            raise WalletError('Unauthorized access')

        existing_wallet = await get_user_wallet(username)
        if existing_wallet:
            raise WalletError('Wallet already exists')

        new_wallet = await create_new_wallet(username)
        if not new_wallet:
            raise WalletError('Failed to create wallet')

        logging.info(f"Created new wallet for user: {username}")
        return {'wallet_id': new_wallet['id'], 'balance': new_wallet['balance']}
    except WalletError as e:
        logging.error(f"Error creating wallet: {str(e)}")
        return {'error': str(e)}

async def deposit_to_wallet(token, amount):
    try:
        username = decode_token(token)
        if not username:
            raise WalletError('Unauthorized access')

        if amount <= 0:
            raise WalletError('Invalid deposit amount')

        wallet = await get_user_wallet(username)
        if not wallet:
            raise WalletError('Wallet not found')

        new_balance = wallet['balance'] + amount
        await update_wallet_balance(username, new_balance)
        await log_transaction(username, 'deposit', amount)
        await trigger_event('deposit', username, amount)

        logging.info(f"Deposited {amount} to wallet for user: {username}")
        return {'new_balance': new_balance}
    except WalletError as e:
        logging.error(f"Error depositing to wallet: {str(e)}")
        return {'error': str(e)}

async def withdraw_from_wallet(token, amount):
    try:
        username = decode_token(token)
        if not username:
            raise WalletError('Unauthorized access')

        if amount <= 0:
            raise WalletError('Invalid withdrawal amount')

        wallet = await get_user_wallet(username)
        if not wallet:
            raise WalletError('Wallet not found')

        if wallet['balance'] < amount:
            raise WalletError('Insufficient funds')

        new_balance = wallet['balance'] - amount
        await update_wallet_balance(username, new_balance)
        await log_transaction(username, 'withdraw', amount)
        await trigger_event('withdraw', username, amount)

        logging.info(f"Withdrew {amount} from wallet for user: {username}")
        return {'new_balance': new_balance}
    except WalletError as e:
        logging.error(f"Error withdrawing from wallet: {str(e)}")
        return {'error': str(e)}
