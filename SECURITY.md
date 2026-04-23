# Security Review: NeoBank Flask Login App

## Summary
Manual code review (Bandit static analysis ran, no report issues).

**Overall Rating: Good for development, Medium for production.** Secure practices used, but needs hardening.

## Findings & Severity

### High (Fix before prod)
1. **Hardcoded SECRET_KEY fallback** (config.py:9)
   - `SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'`
   - Risk: Committed secret.
   - Fix: Remove fallback, set FLASK_SECRET_KEY env var.
   ```
   SECRET_KEY = os.environ['SECRET_KEY']
   ```

2. **DEBUG=True always** (app.py)
   - Uses DevelopmentConfig by default.
   - Risk: Stack traces, debugger in prod.
   - Fix: `if os.environ.get('FLASK_ENV') == 'production': ProductionConfig`
   
3. **Local SQLite** (config.py)
   - File DB vulnerable to host compromise.
   - Fix: PostgreSQL with SSL.

### Medium
1. **No rate limiting on login** (app.py login)
   - Risk: Brute force.
   - Fix: flask-limiter
   ```
   pip install flask-limiter
   from flask_limiter import Limiter
   limiter = Limiter(app, key_func=get_remote_address)
   @app.route('/login', methods=['GET', 'POST'])
   @limiter.limit("5 per minute")
   ```

2. **Weak password policy** (forms.py)
   - Min 8 chars only.
   - Fix: Add regex validator for complexity.

3. **No email verification** 
   - Fix: Add verified flag in User model.

### Low
1. **Long session 24h**
   - Fix: Reduce to 1h, remember_me separate.

2. **No 2FA/admin panel**
   - Add pyotp for TOTP.

## Best Practices Applied ✓
- PBKDF2:sha256 hashing
- CSRF protection (WTF)
- Secure session cookies (HttpOnly, SameSite=Lax)
- Open redirect protection (url_has_allowed_host_and_scheme)
- SQLAlchemy ORM (no inj)
- Jinja auto-escape (no XSS)
- Form validation

## Remediation Priority
1. Env SECRET_KEY, prod config
2. Rate limiting
3. DB migration
4. HTTPS (SESSION_COOKIE_SECURE=True)

Run `bandit -r .` locally for static scan.

App secure for dev/demo use.
