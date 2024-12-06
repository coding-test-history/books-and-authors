from sqlalchemy.orm import Session
from app.models.BooksModel import BooksModel
from app.models.AuthorsModel import AuthorsModel

def seedBooks(db: Session):
    # Ambil data author yang telah tersimpan di database
    authors = db.query(AuthorsModel).all()

    # Data awal buku yang ingin dimasukkan (satu buku per author untuk contoh ini)
    books = [
        {"title": "Book 1", "description": "Description Book 1", "publish_date": "2024-12-01"},
        {"title": "Book 2", "description": "Description Book 2", "publish_date": "2024-12-01"},
        {"title": "Book 3", "description": "Description Book 3", "publish_date": "2024-12-01"},
    ]

    # Pastikan jumlah data books tidak melebihi jumlah authors
    for i, bookData in enumerate(books):
        if i < len(authors):  # Pastikan tidak melebihi jumlah authors yang tersedia
            author = authors[i]
            bookData["author_id"] = author.id  # Set `author_id` dari data author yang sudah ada

            # Periksa apakah buku dengan judul yang sama sudah ada di database
            existing_item = db.query(BooksModel).filter(BooksModel.title == bookData["title"]).first()
            if not existing_item:
                dbBook = BooksModel(**bookData)
                db.add(dbBook)

    db.commit()
    print("Books seeded successfully!")
