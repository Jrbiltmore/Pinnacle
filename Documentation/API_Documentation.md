
# API Documentation

## Overview

This document provides details on the API endpoints available in the Tap'n'Earn system. The API is designed to facilitate secure and efficient financial transactions, user management, and integration with third-party services.

## Authentication

### `POST /api/auth/login`

- **Description**: Authenticates a user and returns a JWT token.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  - `200 OK`: Returns a token on successful authentication.
  - `401 Unauthorized`: Invalid credentials.

### `POST /api/auth/register`

- **Description**: Registers a new user.
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string",
    "email": "string"
  }
  ```
- **Response**:
  - `201 Created`: User registered successfully.
  - `400 Bad Request`: Invalid input data.

## Wallet Management

### `GET /api/wallet`

- **Description**: Retrieves the user's wallet balance.
- **Response**:
  - `200 OK`: Returns the wallet balance.
  - `401 Unauthorized`: Authentication required.

### `POST /api/wallet/transfer`

- **Description**: Transfers funds to another user.
- **Request Body**:
  ```json
  {
    "recipient": "string",
    "amount": "number"
  }
  ```
- **Response**:
  - `200 OK`: Transfer successful.
  - `400 Bad Request`: Insufficient funds or invalid recipient.

## Transactions

### `GET /api/transactions`

- **Description**: Retrieves the user's transaction history.
- **Response**:
  - `200 OK`: Returns a list of transactions.
  - `401 Unauthorized`: Authentication required.

### `POST /api/transactions`

- **Description**: Creates a new transaction.
- **Request Body**:
  ```json
  {
    "type": "string",
    "amount": "number",
    "description": "string"
  }
  ```
- **Response**:
  - `201 Created`: Transaction created successfully.
  - `400 Bad Request`: Invalid input data.

## Error Codes

- `200 OK`: Successful operation.
- `201 Created`: Resource created successfully.
- `400 Bad Request`: Invalid input data.
- `401 Unauthorized`: Authentication required.
- `403 Forbidden`: Access denied.
- `404 Not Found`: Resource not found.
