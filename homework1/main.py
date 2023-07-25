# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
# «Обувь» и «Куртка», используя базовый шаблон.


from flask import Flask, render_template

app = Flask(__name__, static_folder='templates')


@app.route('/')
@app.route('/index/')
def index_page():
    return render_template("/index.html/")


list_dres = [{"name": "Пиджмак", "cost": 1200, "size": 50},
             {"name": "Платье", "cost": 1600, "size": 38},
             {"name": "брюки", "cost": 1000, "size": 48},
             {"name": "шорты", "cost": 600, "size": 50}]
all_shoes = [{"name": "Кросовки", "cost": 1200, "size": 43},
             {"name": "Кеды", "cost": 1700, "size": 45},
             {"name": "Туфли", "cost": 2200, "size": 32}

             ]
hats = [{"name": "Шляпка", "cost": 1200, "size": 34},
        {"name": "Шляпа", "cost": 2000, "size": 45},
        {"name": "Большая Шляпа", "cost": 2500, "size": 43},
        {"name": "Средняя Шляпа", "cost": 1200, "size": 35},
        {"name": "Кепка", "cost": 500, "size": 33},
        {"name": "Панама", "cost": 100, "size": 43}]


@app.route('/dress/')
def dress():
    return render_template("/dress.html/", list_dres=list_dres)


@app.route('/shoes/')
def shoes():
    return render_template("/shoes.html/", all_shoes=all_shoes)


@app.route('/hat/')
@app.route('/hat/<int:num>/')
def hat(num=10000):
    return render_template("/hat.html/", hats=hats, num=num)


if __name__ == '__main__':
    app.run(debug=True)
