"""Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(debug=True)
