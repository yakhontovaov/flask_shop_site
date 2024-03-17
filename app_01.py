from flask import Flask, render_template, request, make_response, redirect, url_for, flash
from form_registr import RegistrationForm
from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'

db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Ok')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация прошла успешно!', 'success')
        response = make_response(redirect(url_for('home')))
        response.set_cookie('user_data', '{}:{}'.format(form.first_name.data, form.last_name.data,
                                                        form.email.data))
        return response
    return render_template('register.html', form=form)


@app.route('/home/')
def home():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, _ = user_data.split(':')
        return render_template('home.html', name=name)
    else:
        return redirect(url_for('index'))


@app.route('/about_us/')
def about_us():
    return render_template('about_us.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/cloth/')
def cloth():
    return render_template('cloth.html')


@app.route('/shoes/')
def shoes():
    return render_template('shoes.html')


@app.route('/accessories/')
def accessories():
    return render_template('accessories.html')


@app.route('/exit/')
def exit_():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_data', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
