from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import DateTime, ForeignKey
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    tablename = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    

# Relationships
roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))
reminders = db.relationship('Reminder', backref='user', lazy='dynamic')

def __repr__(self):
    return f"<User(username='{self.username}')>"
class Role(db.Model):
    tablename = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

def __repr__(self):
    return f"<Role(name='{self.name}')>"
user_roles = db.Table('user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)

class Organization(db.Model):
    tablename = 'organization'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    contact_information = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    isAdminApproved = db.Column(db.Boolean, default=False)  

# Relationships
donations = db.relationship('Donation', backref='organization', lazy='dynamic')
stories = db.relationship('Story', backref='organization', lazy='dynamic')
beneficiaries = db.relationship('Beneficiary', backref='organization', lazy='dynamic')
reminders = db.relationship('Reminder', backref='organization', lazy='dynamic')

def __repr__(self):
    return f"<Organization(name='{self.name}')>"
class Donation(db.Model):
    tablename = 'donation'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    donor_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    donation_type = db.Column(db.String(50), nullable=False)
    anonymous = db.Column(db.Boolean, default=False)
    date = db.Column(db.Date, nullable=False)
    transaction_id = db.Column(db.String(120), unique=True, nullable=True)  # Optional field for transaction ID

def __repr__(self):
    return f"<Donation(amount={self.amount})>"
class Story(db.Model):
    tablename = 'story'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    images = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return f"<Story(title='{self.title}')>"
class Beneficiary(db.Model):
    tablename = 'beneficiary'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    inventory_received = db.Column(db.Text, nullable=False)

# Relationships
inventories = db.relationship('Inventory', backref='beneficiary', lazy='dynamic')

def __repr__(self):
    return f"<Beneficiary(name='{self.name}')>"
class Inventory(db.Model):
    tablename = 'inventory'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    beneficiary_id = db.Column(db.Integer, db.ForeignKey('beneficiary.id'))
    description = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    date_received = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return f"<Inventory(description='{self.description}')>"
class Reminder(db.Model):
    tablename = 'reminder'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'))
    remind_on = db.Column(db.Date, nullable=False)
    message = db.Column(db.Text, nullable=False)

def __repr__(self):
    return f"<Reminder(user_id={self.user_id}, organization_id={self.organization_id})>"