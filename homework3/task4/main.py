from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from task4.forms import RegistrationForm
from task4.models import db, User
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///users.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/')
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        existing_email = User.query.filter(email == User.email).first()
        # так как бывают люди с одинаковыми именами и фамилиями то проверяем на уникальность только почту
        if existing_email:
            error_msg = 'User or email already exists.'
            form.username.errors.append(error_msg)
            return render_template('register.html', form=form)
        hashed_password = generate_password_hash(password)
        # hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_user = User(username=username,lastname=lastname, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        success_msg = 'Registration successful!'
        return success_msg

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
