from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# =========================
# HOME / LOGIN PAGE
# =========================

@app.route('/')
def home():
    return render_template('login.html')


# =========================
# LOGIN FUNCTION
# =========================

@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']

    print("Email:", email)
    print("Password:", password)

    return redirect('/dashboard')


# =========================
# SIGNUP PAGE
# =========================

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup-user', methods=['POST'])
def signup_user():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

    return redirect('/')

# =========================
# DASHBOARD PAGE
# =========================

@app.route('/dashboard')
def dashboard():

    trips = [
        {
            "name": "Goa Trip",
            "date": "12 May - 18 May",
            "budget": 25000
        },

        {
            "name": "Manali Adventure",
            "date": "20 June - 28 June",
            "budget": 40000
        }
    ]

    return render_template(
        'dashboard.html',
        trips=trips
    )


# =========================
# CREATE TRIP PAGE
# =========================

@app.route('/create-trip')
def create_trip():
    return render_template('create_trip.html')


# =========================
# MY TRIPS PAGE
# =========================

@app.route('/trips')
def trips():
    return render_template('trips.html')


# =========================
# RUN APP
# =========================

if __name__ == '__main__':
    app.run(debug=True)