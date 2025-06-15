import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Production Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///placement_tracker.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    cards = db.relationship('Card', backref='user', lazy=True)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    package = db.Column(db.String(50))
    status = db.Column(db.String(20), default='Applied')

# Create tables
with app.app_context():
    db.create_all()

# Authentication Routes
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('signup.html', error='Email already exists')
        
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Create new user
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        # Log the user in
        session['user_id'] = new_user.id
        return redirect(url_for('dashboard'))
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

# Dashboard and Card Management Routes
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    cards = Card.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', cards=cards)

@app.route('/add_card', methods=['POST'])
def add_card():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    data = request.json
    new_card = Card(
        user_id=session['user_id'],
        company=data['company'],
        role=data['role'],
        description=data.get('description', ''),
        package=data.get('package', ''),
        status=data.get('status', 'Applied')
    )
    
    db.session.add(new_card)
    db.session.commit()
    
    return jsonify({
        'id': new_card.id,
        'company': new_card.company,
        'role': new_card.role,
        'description': new_card.description,
        'package': new_card.package,
        'status': new_card.status
    }), 201

@app.route('/update_card/<int:card_id>', methods=['POST'])
def update_card(card_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    card = Card.query.get_or_404(card_id)
    
    # Ensure the card belongs to the current user
    if card.user_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.json
    card.status = data.get('status', card.status)
    card.company = data.get('company', card.company)
    card.role = data.get('role', card.role)
    card.description = data.get('description', card.description)
    card.package = data.get('package', card.package)
    
    db.session.commit()
    
    return jsonify({
        'id': card.id,
        'company': card.company,
        'role': card.role,
        'description': card.description,
        'package': card.package,
        'status': card.status
    }), 200

@app.route('/delete_card/<int:card_id>', methods=['POST'])
def delete_card(card_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    card = Card.query.get_or_404(card_id)
    
    # Ensure the card belongs to the current user
    if card.user_id != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    db.session.delete(card)
    db.session.commit()
    
    return jsonify({'message': 'Card deleted successfully'}), 200

if __name__ == '__main__':
    # Ensure database is created
    with app.app_context():
        db.create_all()
    
    # Use different port for production if specified
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 