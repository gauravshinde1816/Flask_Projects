from flask import Flask , render_template , url_for , flash , redirect
from forms import RegistrationForm , LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1fdsdfl6@kip4ydbsr1qh@3xfs=wl08@tnrir)sd#4#pgx(jry5uj&9k5ewe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register' , methods=['GET' , "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account is created for {form.username.data}!' ,'success')
        return redirect(url_for('index'))

    return render_template('register.html' , title='register' ,form =form )


@app.route('/login' , methods=['GET' , "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "gauravshinde@gmail.com" and form.password.data == 'password':
            flash(f"You are logged in successfully!" , 'success')
            return redirect(url_for('index'))
        else:
            flash(f"Enter correct credentials",'danger')
    return render_template('login.html' , title='login' ,form =form )


if __name__ == '__main__':
    app.run(debug=True)