from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome/', methods=['POST'])
def welcome():
    name = request.form.get('name')
    email = request.form.get('email')

    if name and email:
        response = make_response(redirect(url_for('home')))
        response.set_cookie('user_data', f'{name}:{email}')
        return response
    else:
        return redirect(url_for('index'))


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
