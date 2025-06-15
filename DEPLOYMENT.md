# Placement Tracker Deployment Guide 🚀

## Deployment Options

### 1. Local Deployment
1. Clone the repository
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python app.py
```

### 2. Heroku Deployment
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Install Heroku CLI
2. Login to Heroku
```bash
heroku login
```
3. Create Heroku app
```bash
heroku create placement-tracker-app
```
4. Set environment variables
```bash
heroku config:set SECRET_KEY=your_secret_key
```
5. Push to Heroku
```bash
git push heroku main
```

### 3. PythonAnywhere Deployment
1. Create a PythonAnywhere account
2. Open a Bash console
```bash
git clone https://github.com/yourusername/placement-tracker.git
cd placement-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Configure WSGI file in PythonAnywhere Web tab

### 4. DigitalOcean App Platform
1. Create a DigitalOcean account
2. Connect GitHub repository
3. Configure app settings
4. Deploy with one click

## Environment Variables
- `SECRET_KEY`: Flask secret key
- `DATABASE_URL`: Database connection string
- `PORT`: Application port (default: 5000)

## Troubleshooting
- Ensure all dependencies are installed
- Check database migrations
- Verify environment configurations

## Security Recommendations
- Use strong, unique secret keys
- Enable HTTPS
- Implement rate limiting
- Regularly update dependencies 