@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        # Retrieve user-specific data from the database
        return f'Welcome {username}'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

