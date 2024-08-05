
import React from 'react';

export default function Navbar() {
  return (
    <nav style={styles.navbar}>
      <div style={styles.logo}>Tap'n'Earn</div>
      <ul style={styles.navLinks}>
        <li style={styles.navItem}><a href="/">Home</a></li>
        <li style={styles.navItem}><a href="/wallet">Wallet</a></li>
        <li style={styles.navItem}><a href="/transactions">Transactions</a></li>
        <li style={styles.navItem}><a href="/profile">Profile</a></li>
      </ul>
    </nav>
  );
}

const styles = {
  navbar: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#6200EE',
    padding: '10px 20px',
  },
  logo: {
    color: '#FFFFFF',
    fontSize: '24px',
    fontWeight: 'bold',
  },
  navLinks: {
    display: 'flex',
    listStyleType: 'none',
  },
  navItem: {
    margin: '0 10px',
  },
};
