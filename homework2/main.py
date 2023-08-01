# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке
# которой будет создан cookie-файл с данными пользователя, а также будет произведено перенаправление
# на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл
# с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.


from flask import Flask, render_template, request, url_for, redirect, make_response

app = Flask(__name__, static_folder='templates')


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['lastName']
        email = request.form['email']
        response = make_response(redirect(url_for('hello', name=name)))
        response.set_cookie('user_name', name)
        response.set_cookie('email', email)
        return response
    return render_template("index.html")

@app.route('/hello')
def hello():
    name_user = request.args.get("name")
    return render_template('/hello.html/', name_user=name_user)


@app.route('/getcookie/')
def get_cookies():
    name = request.cookies.get('user_name')
    email = request.cookies.get('email')
    return f"Значение cookie: для пользователя {name}  электронная почта {email}"


@app.route('/del_cookies/')
def del_cookies():
    res = make_response(redirect(url_for('index')))
    res.set_cookie('user_name',max_age=0)
    res.set_cookie("email",max_age=0)
    return res



if __name__ == '__main__':
    app.run(debug=True)
