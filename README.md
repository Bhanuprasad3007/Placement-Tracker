# Placement Tracker 🚀

## Overview
Placement Tracker is a web application designed to help students and job seekers manage their job application process using a Kanban-style board.

## 🌟 Features
- User Authentication (Signup/Login)
- Kanban-style Job Application Tracking
- Add, Edit, and Delete Job Applications
- Responsive Design

## 🛠 Technologies Used
- Backend: Flask (Python)
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- Authentication: Flask-Bcrypt
- ORM: SQLAlchemy

## 🚀 Deployment Options

### Local Development
1. Clone the repository
```bash
git clone https://github.com/yourusername/placement-tracker.git
cd placement-tracker
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file in the project root with:
```
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///placement_tracker.db
```

5. Run the application
```bash
python app.py
```

### Deployment Platforms

#### Heroku
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Create a `Procfile`
```
web: gunicorn app:app
```

2. Create `runtime.txt`
```
python-3.9.13
```

#### PythonAnywhere
1. Upload project files
2. Create a new web app
3. Set up WSGI configuration to point to your Flask app

#### Render
1. Connect your GitHub repository
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `gunicorn app:app`

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact
Your Name - youremail@example.com

Project Link: [https://github.com/yourusername/placement-tracker](https://github.com/yourusername/placement-tracker) 