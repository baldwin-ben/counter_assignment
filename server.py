from flask import Flask, render_template, request, redirect, session # don't forget to import redirect!
app = Flask(__name__)
app.secret_key = "There are no secrets on GitHub" #tp use sessions we need a secret key

@app.route('/')
def count():
    if not "count" in session: # if count is not in session, session = session + 1. 
        session['count'] = 1
    else:
        session['count'] += 1 #reset session to 1
    return render_template('index.html', count=session["count"])

@app.route('/add', methods=["POST"])
def add():
    session['count'] += 1
    return redirect ('/') # this route adds 1 to count and the redirect adds 1 to count, which is how we achieve the +2 button.

@app.route('/destroy', methods=["GET"]) #GET is default so its not needed.
def destroy():
    session['count'] = 0
    return redirect ('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.