# Quick Start Guide

## Running the Flask Login System

### 1. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`

### 3. Access the Application

Open your browser and navigate to:
- **Home**: http://127.0.0.1:5000
- **Register**: http://127.0.0.1:5000/register
- **Login**: http://127.0.0.1:5000/login

### 4. Create a Test Account

1. Go to the Registration page
2. Create a new account with:
   - Username: `testuser`
   - Email: `test@example.com`
   - Password: `TestPassword123` (min 8 characters)
3. Log in with your credentials

### 5. Security Features to Explore

- **Password Hashing**: Check the console for hashed passwords in database
- **CSRF Protection**: All forms include CSRF tokens (view page source)
- **Session Management**: Cookies are HTTPOnly and SameSite
- **Input Validation**: Try submitting invalid data
- **Open Redirect Prevention**: Check the login redirect logic

## Database

The application uses SQLite by default. The database file is created as `login_system.db` in the project root.

To reset the database, simply delete the `login_system.db` file and run the app again.

## File Structure

```
.
├── .github/
│   └── copilot-instructions.md
├── .env.example
├── README.md
├── QUICKSTART.md (this file)
├── app.py               # Main Flask application
├── config.py            # Configuration settings
├── models.py            # Database models (User)
├── forms.py             # Form definitions and validation
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Home page
│   ├── login.html       # Login form
│   ├── register.html    # Registration form
│   ├── dashboard.html   # User dashboard
│   ├── change_password.html
│   ├── 404.html         # 404 error page
│   └── 500.html         # 500 error page
├── static/
│   └── css/
│       └── style.css    # Main stylesheet
└── venv/                # Virtual environment (created during setup)
```

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='127.0.0.1', port=5001)
```

### Database Issues
If you encounter database errors, delete `login_system.db` and restart the app.

### Import Errors
Make sure the virtual environment is activated:
- Check the command prompt shows `(venv)` prefix
- If not, run the activation command again

## Development Tips

1. **Auto-reload**: Debug mode is enabled in development, so the app will reload when you save files
2. **Database Explorer**: Install a SQLite browser to view the database
3. **Form Debugging**: Use browser DevTools to inspect CSRF tokens in form source
4. **Password Testing**: Try the "Change Password" feature on the dashboard

## Next Steps for Learning

1. Study the CSRF protection in `forms.py` and templates
2. Examine password hashing in `models.py`
3. Review session configuration in `config.py`
4. Explore Flask-Login integration in `app.py`
5. Check form validation in `forms.py`

## Security Considerations for Production

- Change `SECRET_KEY` in `config.py`
- Use environment variables for sensitive data
- Enable HTTPS and `SESSION_COOKIE_SECURE`
- Use PostgreSQL instead of SQLite
- Implement rate limiting
- Add logging and monitoring
- Consider using Flask-Security for more features
