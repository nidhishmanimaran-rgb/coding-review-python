# Flask Login System

A secure, production-ready login system built with Flask for educational purposes and security study.

## Features

- **User Authentication**: Secure login and registration system
- **Password Hashing**: PBKDF2:SHA256 hashing with Werkzeug
- **Session Management**: Secure HTTP-only, SameSite cookies
- **CSRF Protection**: Flask-WTF CSRF tokens on all forms
- **Input Validation**: Comprehensive form validation with WTForms
- **Database**: SQLAlchemy ORM with SQLite
- **Responsive Design**: Bootstrap-inspired CSS styling

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone or download the project
2. Navigate to the project directory
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
.
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── models.py               # Database models
├── forms.py                # Form definitions with validation
├── requirements.txt        # Python dependencies
├── static/
│   └── css/
│       └── style.css       # Main stylesheet
└── templates/
    ├── base.html           # Base template with navigation
    ├── index.html          # Home page
    ├── login.html          # Login form
    ├── register.html       # Registration form
    ├── dashboard.html      # User dashboard
    ├── change_password.html # Change password form
    ├── 404.html            # 404 error page
    └── 500.html            # 500 error page
```

## Configuration

Edit `config.py` to configure:
- `SECRET_KEY`: Change for production
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `SESSION_COOKIE_SECURE`: Enable HTTPS in production
- `PERMANENT_SESSION_LIFETIME`: Session duration

## Running the Application

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000`

## Default Test Account

After running the application, you can create a new account or use the registration page to test.

## Security Features

1. **Password Hashing**: Passwords are hashed using PBKDF2:SHA256
2. **CSRF Protection**: All forms include CSRF tokens
3. **Session Security**: 
   - HTTPOnly cookies prevent JavaScript access
   - SameSite attribute prevents CSRF attacks
   - Secure flag enabled in production
4. **Input Validation**: All inputs are validated
5. **Open Redirect Prevention**: Redirect URLs are validated
6. **SQL Injection Prevention**: SQLAlchemy parameterized queries

## Development vs Production

### Development
- Debug mode enabled
- Insecure cookies for local testing
- SQLite database

### Production
- Debug mode disabled
- Secure cookies required
- Should use PostgreSQL or MySQL
- Set `FLASK_ENV=production`

## Learning Resources

This project demonstrates:
- Flask web framework fundamentals
- SQLAlchemy ORM usage
- WTForms form handling and validation
- Password hashing and verification
- Session management
- CSRF protection
- Responsive web design

## Future Enhancements

- Email verification on registration
- Password reset functionality
- Two-factor authentication
- User roles and permissions
- Activity logging
- Account lockout after failed attempts
- Rate limiting on login attempts

## License

Educational project for security study.

## Disclaimer

This is an educational project. For production systems, consider:
- Using established authentication libraries (e.g., Flask-Security)
- Implementing rate limiting
- Adding email verification
- Using HTTPS in production
- Implementing proper logging and monitoring
- Regular security audits
