# HTTPS and Security Configuration
- Enabled SECURE_SSL_REDIRECT for HTTPS enforcement.
- Set SECURE_HSTS_SECONDS=31536000, INCLUDE_SUBDOMAINS, and PRELOAD for HSTS.
- Configured SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE for secure cookies.
- Added secure headers: X_FRAME_OPTIONS='DENY', SECURE_CONTENT_TYPE_NOSNIFF, SECURE_BROWSER_XSS_FILTER.
- Nginx configuration provided for SSL/TLS setup.
- Tested HTTPS redirects and secure cookie transmission.
