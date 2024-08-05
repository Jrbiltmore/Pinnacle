
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))

    wallet = relationship("Wallet", back_populates="user")

class Wallet(Base):
    __tablename__ = 'wallets'
    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    user = relationship("User", back_populates="wallet", uselist=False)

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default='pending')

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])

class QuantumTransaction(Base):
    __tablename__ = 'quantum_transactions'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    recipient_public_key = Column(String, nullable=False)
    encrypted_symmetric_key = Column(String, nullable=False)
    iv = Column(String, nullable=False)
    encrypted_message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    sender = relationship("User", foreign_keys=[sender_id])

# Database setup
engine = create_engine('sqlite:///tapnearn.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
