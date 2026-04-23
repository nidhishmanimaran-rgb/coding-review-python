# Complete NeoBank Secure Login App & Security Audit Report

## 1. Project Overview
**NeoBank** - Professional Flask login system rebranded from generic demo.

**Features:**
- User registration/login/logout
- Dashboard with profile info
- Password change
- Secure sessions/CSRF
- Responsive banking UI (green theme)

**Tech Stack:**
- Flask 2.3.3
- Flask-Login 0.6.2
- Flask-WTF 1.1.1 (CSRF)
- Flask-SQLAlchemy 3.0.5 (SQLite)
- Werkzeug secure hashing

**Run:**
```
python run_app.py  # Opens browser to http://127.0.0.1:5000
```

## 2. File Structure
```
e:/python/
├── app.py (routes/auth)
├── models.py (User model PBKDF2)
├── forms.py (WTF validation)
├── config.py (env configs)
├── templates/*.html (Jinja banking UI)
├── static/css/style.css (green banking theme)
├── SECURITY
