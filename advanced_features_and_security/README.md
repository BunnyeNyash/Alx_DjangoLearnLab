# Security Best Practices
- Configured secure settings: DEBUG=False, SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, etc.
- CSRF tokens included in all forms.
- ORM used to prevent SQL injection; inputs validated via Django forms.
- CSP implemented to mitigate XSS risks.
- Tested for CSRF, XSS, and input validation vulnerabilities.
