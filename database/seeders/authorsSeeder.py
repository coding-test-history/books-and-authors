from sqlalchemy.orm import Session
from app.models.AuthorsModel import AuthorsModel

def seedAuthors(db: Session):
    # Data awal yang ingin dimasukkan
    authors = [
        {"name": "Author 1", "bio": "Bio Author 1", "birth_date": "2024-12-01"},
        {"name": "Author 2", "bio": "Bio Author 2", "birth_date": "2024-12-01"},
        {"name": "Author 3", "bio": "Bio Author 3", "birth_date": "2024-12-01"},
    ]

    # Memasukkan data ke database
    for authorData in authors:
        existing_item = db.query(AuthorsModel).filter(AuthorsModel.name == authorData["name"]).first()
        if not existing_item:
            dbAuthor = AuthorsModel(**authorData)
            db.add(dbAuthor)

    db.commit()
    print("Authors seeded successfully!")
