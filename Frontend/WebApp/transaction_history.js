
document.addEventListener("DOMContentLoaded", function () {
  fetchTransactions();
});

function fetchTransactions() {
  const token = getAuthToken();
  fetch('/api/transactions', {
    method: 'GET',
    headers: {
      'Authorization': \`Bearer \${token}\`
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.error) {
      console.error("Error fetching transactions:", data.error);
      alert("Failed to retrieve transaction history.");
    } else {
      displayTransactions(data.transactions);
    }
  })
  .catch(error => console.error("Error:", error));
}

function displayTransactions(transactions) {
  const transactionList = document.getElementById("transaction-list");
  if (transactionList) {
    transactionList.innerHTML = ''; // Clear existing list
    transactions.forEach(transaction => {
      const listItem = document.createElement('li');
      listItem.textContent = \`\${transaction.date}: \${transaction.type} $\${transaction.amount} - \${transaction.status}\`;
      transactionList.appendChild(listItem);
    });
  }
}

function getAuthToken() {
  // Placeholder for retrieving auth token from local storage or cookies
  return "your-auth-token";
}
