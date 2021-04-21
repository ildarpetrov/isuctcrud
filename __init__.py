from flask import Flask, request, render_template, redirect
from .models import db, BookModel
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://user123:password@localhost:5432/pythonBase"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Показать домашнюю страницу
@app.route('/')
def home():
    return render_template('home.html', title="Добро пожаловать в админ панель!")

# Показать страницу с полным списком книг
@app.route('/books', methods=["GET"])
def books():
    books = BookModel.getBooks()
    return render_template('index.html', title="Полный список книг", books=books)

# Показать книгу по её id
@app.route('/book/<int:bookId>', methods=["GET"])
def getBook(bookId):
    book = BookModel.getBook(bookId)
    return render_template('show.html', title="Книга " + book.name, book=book)

# Показать форму создания новой книги
@app.route('/book/create', methods=["GET"])
def formCreate():
    return render_template('create.html', title="Форма создания книги")

# Создание новой книги
@app.route('/book/create', methods=["POST"])
def create():
    ex = BookModel(request.form['isbn'], request.form['name'], request.form['author'], request.form['pages'], request.form['year'])
    book = ex.createBook()
    return redirect('/books')

# Показать форму обновления/редактирования книги
@app.route('/book/update/<int:bookId>', methods=["GET"])
def formUpdate(bookId):
    book = BookModel.getBook(bookId)
    return render_template('update.html', title="Форма редактирования/обновления книги " + book.name, book=book)

# Обновить данные книги
@app.route('/book/update/<int:bookId>', methods=["POST"])
def update(bookId):
    ex = BookModel(request.form['isbn'], request.form['name'], request.form['author'], request.form['pages'], request.form['year'])
    book = ex.updateBook(bookId)
    return redirect('/books')

# Удалить книгу
@app.route('/book/delete/<int:bookId>', methods=["POST"])
def delete(bookId):
    book = BookModel.deleteBook(bookId)
    return redirect('/books')

if __name__ == '__main__':
    app.run(debug=True)