#FLASK - мінімалістичний фреймворк
from flask import Flask, render_template, request

app = Flask(__name__)
# params , query params
# http://localhost:5000/product/23
products = ['bread', 'milk', 'tomato', 'eggs']

@app.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    title = data['title']
    products.append(title)
    return {
        'title': title,
    },201


@app.route('/product/<int:id>')
def product_by_id(id):
    return f'Your product with id {id} {products[id-1]}'

@app.route('/product/<title>')
def product_by_title(title):
    return f'Your product with id {title} '


# http://localhost:5000/product?id=23
@app.route('/product')
def product_by_id_qp():
    answer = ''
    for el in products:
        answer += f'{el} '
    return answer




@app.route('/index')
@app.route('/')
def home():
    menu = ['Головна','Каталог','Про нас','Доставка','Контакти']
    return render_template('index.html', title='Home',menu=menu)


if __name__ == '__main__':
    app.run(debug=True)