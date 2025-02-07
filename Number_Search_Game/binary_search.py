from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__, template_folder="templates")
app.secret_key = 'supersecretkey'  # Required for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'low' not in session or 'high' not in session:
        session['low'] = 1
        session['high'] = 100
        session['attempts'] = 0

    if request.method == 'POST':
        session['attempts'] += 1
        user_input = request.form['response']
        guess = (session['low'] + session['high']) // 2

        if user_input == 'higher':
            session['low'] = guess + 1
        elif user_input == 'lower':
            session['high'] = guess - 1
        elif user_input == 'correct':
            return render_template('index.html', guess=guess, attempts=session['attempts'], game_over=True)
        
        if session['low'] > session['high']:
            return render_template('index.html', error="Oops! Did you change your number?", game_over=True)
        
    guess = (session['low'] + session['high']) // 2
    return render_template('index.html', guess=guess, attempts=session['attempts'])

@app.route('/reset')
def reset():
    session.clear()  # Clears all session variables
    return redirect(url_for('index'))  # Redirects back to the start

if __name__ == "__main__":
    app.run(debug=True)
