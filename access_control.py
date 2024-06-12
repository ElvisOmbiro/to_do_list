@app.route('/todos', methods=['GET', 'POST'])
def manage_todos():
    if 'username' in session:
        username = session['username']
        # Fetch or save to-do items specific to the logged-in user
        return 'User-specific to-do list'

