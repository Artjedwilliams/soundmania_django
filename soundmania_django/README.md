# Sound Mania — Django Authentication

A responsive login and registration UI inspired by the supplied reference images.

## Features
- Create account with first name, last name, email, and password confirmation
- Email-based login
- Remember-me session option
- Password reset flow (development email is printed in the terminal)
- Django password hashing, CSRF protection, and session authentication
- Responsive split-screen design using your supplied logo and illustration

## 1. Open in Visual Studio Code
Extract `soundmania_django.zip`, then open the extracted `soundmania_django` folder in VS Code.

## 2. Create and activate a virtual environment

**Windows PowerShell**
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

## 3. Install Django
```powershell
pip install -r requirements.txt
```

## 4. Create the database tables
```powershell
python manage.py migrate
```

## 5. Start the development server
```powershell
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## Notes
- Register at `/register/`, then log in using your email and password.
- Password reset is available through **Forgot Password?**. Since this project uses Django's console email backend, the reset email/link appears in the VS Code terminal.
- The Terms of Service and Privacy Policy links are placeholders. Replace `href="#"` in `templates/accounts/register.html` when you have actual policy pages.
- This setup is for local development. Before deployment, set `DEBUG = False`, configure a secure `SECRET_KEY`, `ALLOWED_HOSTS`, HTTPS, and a real email provider.
