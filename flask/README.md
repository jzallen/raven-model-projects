# Flask Portfolio Application

A modular Flask application with dynamic module loading and user authentication.

## Structure

```
flask/
├── app.py                    # Main application entry point
├── config.py                 # Configuration (env variables, etc.)
├── requirements.txt          # Python dependencies
├── modules/                  # Directory containing all feature blueprints
│   └── user_login/           # User authentication module
│       ├── __init__.py
│       ├── routes.py
│       └── templates/
│           └── user_login/
│               └── login.html
├── static/                   # Static files (CSS, JS, images)
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── templates/                # Common templates shared by modules
    ├── base.html
    └── index.html
```

## Features

- **Modular Architecture**: Built with Flask blueprints for easy module management
- **Dynamic Module Loading**: Configure which modules to load in `app.py`
- **User Authentication**: Login/logout functionality with session management
- **Responsive Design**: Bootstrap 5 for mobile-first responsive design
- **Flash Messages**: User feedback system
- **Custom Styling**: Enhanced UI with custom CSS

## Getting Started

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and go to `http://127.0.0.1:5000`

### Demo Login

- **Username**: admin
- **Password**: password

## Adding New Modules

1. Create a new directory in `modules/` (e.g., `modules/blog/`)
2. Add `__init__.py`, `routes.py`, and templates
3. Create a blueprint in `routes.py` named `bp`
4. Add the module name to `modules_to_load` list in `app.py`

### Example Module Structure

```python
# modules/your_module/routes.py
from flask import Blueprint, render_template

bp = Blueprint('your_module', __name__, url_prefix='/your_module')

@bp.route('/')
def index():
    return render_template('your_module/index.html')
```

## Configuration

Environment variables can be set in `config.py`:

- `SECRET_KEY`: Flask secret key for sessions
- `FLASK_DEBUG`: Enable/disable debug mode
- `DATABASE_URL`: Database connection string (if using a database)

## Development

The application runs in debug mode by default, which includes:
- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger

## Production Deployment

For production:
1. Set `FLASK_DEBUG=False`
2. Use a production WSGI server (gunicorn, uWSGI)
3. Set a secure `SECRET_KEY`
4. Configure proper database settings
