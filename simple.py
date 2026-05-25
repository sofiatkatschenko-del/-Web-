from flask import Flask, jsonify

app = Flask(__name__)

# Ваші дані про книги
goods = []

g1 = {"name": "Шістка воронів", "author": "Лі Бардуго", "price": 499, "rating": 4.9, "status": "в наявності"}
g2 = {"name": "Трон зі скла", "author": "Сара Дж. Мас", "price": 579, "rating": 4.8, "status": "в наявності"}
g3 = {"name": "Народ повітря", "author": "Голі Блек", "price": 459, "rating": 5.0, "status": "в наявності"}
g4 = {"name": "Вбивство у 'Східному експресі'", "author": "Агата Крісті", "price": 399, "rating": 4.7, "status": "в наявності"}
g5 = {"name": "48 законів влади", "author": "Руберт Грін", "price": 690, "rating": 4.6, "status": "в наявності"}

goods.append(g1)
goods.append(g2)
goods.append(g3)
goods.append(g4)
goods.append(g5)

# Маршрут, який вимагає вчитель у 3-му пункті
@app.route('/goods')
def get_goods():
    return jsonify(goods)

if __name__ == '__main__':
    app.run(debug=True)
