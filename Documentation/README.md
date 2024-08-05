
# Tap'n'Earn System

## Overview

Tap'n'Earn is a decentralized financial platform that enables users to earn rewards through various financial activities, including transactions, staking, and lending. The platform integrates with quantum-safe technologies to ensure secure and efficient operations.

## Features

- Secure wallet management with quantum-safe encryption
- Integration with Plaid for financial data
- Automated trading and lending strategies
- Customizable credit lines and financial instruments
- Real-time monitoring with Prometheus and Grafana

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.x

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/tapnearn.git
   cd tapnearn
   ```

2. **Build and start the services:**

   ```bash
   docker-compose up --build
   ```

3. **Access the application:**

   - API: `http://localhost:5000`
   - Grafana: `http://localhost:3000`

### Running Tests

To run the tests, use the following commands:

```bash
docker-compose run --rm api pytest tests/UnitTests
docker-compose run --rm api pytest tests/E2ETests
```

## Contributing

We welcome contributions to improve the Tap'n'Earn platform. Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
