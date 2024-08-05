
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import WalletScreen from './WalletScreen';
import TransactionScreen from './TransactionScreen';
import Navbar from './Components/Navbar';
import Footer from './Components/Footer';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Navbar />
      <Stack.Navigator initialRouteName="Wallet">
        <Stack.Screen name="Wallet" component={WalletScreen} />
        <Stack.Screen name="Transactions" component={TransactionScreen} />
      </Stack.Navigator>
      <Footer />
    </NavigationContainer>
  );
}
