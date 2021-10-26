from flask import Flask, request, current_app, redirect

app = Flask('__name__')

@app.route('/') #отрисовка шаблона с помощью render_template()
def index():
    name, age, profession, city = "Max", 24 "years", "Programmer", "Moscow"
    template_context = dict(name=name, age=age, profession=profession, city=city)
    return render_template('index.html', **template_context)

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return "Страничка пользователя №-{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return 'Все книги в категории "<u>{}</u>"'.format(genre)
res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/') #возвращаем ошибку 404
def http_404_handler():
    return make_response("<h2>404 Error</h2>", 400)

@app.route('/set-cookie')# устанавливаем два куки в клиентском браузере
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue")
    res.set_cookie("favorite-font", "sans-serif")
    return res
@app.route('/') #указываем заголовки с помощью кортежей
def render_markdown():
    return "## Heading", 200, {'Content-Type': 'text/markdown'}

@app.route('/transfer')#перенаправляем клиента с помощью redirect вместо "", 302, 
def transfer():
    return "", 302, {'location': 'https://localhost:5000/login'}



if __name__ == "__main__":
    app.run(debug=True)
