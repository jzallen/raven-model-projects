from flask import Blueprint, render_template, request, redirect, url_for, flash, session

# Create blueprint for user_login module
bp = Blueprint('user_login', __name__, url_prefix='/auth',
               template_folder='templates')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Basic validation (replace with actual authentication logic)
        if username and password:
            if username == 'admin' and password == 'password':  # Demo credentials
                session['user_id'] = username
                flash('Login successful!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid username or password', 'error')
        else:
            flash('Please fill in all fields', 'error')

    return render_template('user_login/login.html')


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))
