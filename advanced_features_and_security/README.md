# Security Best Practices
- Configured secure settings: DEBUG=False, SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, etc.
- CSRF tokens included in all forms.
- ORM used to prevent SQL injection; inputs validated via Django forms.
- CSP implemented to mitigate XSS risks.
- Tested for CSRF, XSS, and input validation vulnerabilities.


# Permissions and Groups Setup
- Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) added to the Book model.
- Groups: Editors (create, edit), Viewers (view), Admins (all permissions).
- Use `python manage.py setup_groups` to initialize groups and permissions.
- Views are secured with `@permission_required` decorators.
