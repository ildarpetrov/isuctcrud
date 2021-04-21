from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer(), index=True, primary_key=True)
    isbn = db.Column(db.String())
    name = db.Column(db.String())
    author = db.Column(db.String())
    pages = db.Column(db.Integer())
    year = db.Column(db.Integer())
    created_at = db.Column(db.Date(), default=datetime.now())
    updated_at = db.Column(db.Date(), default=datetime.now())

    def __init__(self, isbn, name, author, pages, year):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.pages = pages
        self.year = year

    def getBook(bookId):
        book = db.session.query(BookModel).filter(BookModel.id == bookId).first()
        return book

    def getBooks():
        books = db.session.query(BookModel).order_by(BookModel.created_at.desc()).all()
        return books

    def createBook(self):
        book = BookModel(self.isbn, self.name, self.author, self.pages, self.year)
        db.session.add(book)
        db.session.commit()
        return book

    def updateBook(self, bookId):
        book = db.session.query(BookModel).filter(BookModel.id == bookId).first()

        book.isbn = self.isbn
        book.name = self.name
        book.author = self.author
        book.pages = self.pages
        book.year = self.year
        book.updated_at = datetime.now()

        db.session.add(book)
        db.session.commit()

        return book

    def deleteBook(bookId):
        book = db.session.query(BookModel).filter(BookModel.id == bookId).first()
        db.session.delete(book)
        db.session.commit()

        return True

    def __repr__(self):
        return f"{self.isbn}:{self.name}:{self.author}:{self.pages}:{self.year}"
