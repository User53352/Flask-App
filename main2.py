from flask import Flask

app = Flask('__name__')

@app.route('/')

def index():
    return "Hello Flask"

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return "Страничка пользователя №-{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    return 'Все книги в категории "<u>{}</u>"'.format(genre)

if __name__ == "__main__":
    app.run(debug=True)
