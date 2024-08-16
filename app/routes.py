from flask import render_template, request
from app import app


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        age = request.form.get('age')

        # Передаем данные в шаблон
        return render_template('form.html', name=name, city=city, hobby=hobby, age=age)

    # Если метод GET, просто рендерим шаблон
    return render_template('form.html')
