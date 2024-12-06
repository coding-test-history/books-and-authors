from sqlalchemy.orm import Session
from app.models.UsersModel import UsersModel
from passlib.hash import bcrypt

def seedUsers(db: Session):
    # Data awal yang ingin dimasukkan
    users = [
        {"name": "User 1", "email": "user1@mail.com", "username": "user1"},
        {"name": "User 2", "email": "user2@mail.com", "username": "user2"},
        {"name": "User 3", "email": "user3@mail.com", "username": "user3"},
    ]

    # Default password untuk semua pengguna
    default_password = "password"

    # Memasukkan data ke database
    for userData in users:
        # Periksa apakah pengguna dengan username atau email yang sama sudah ada
        existing_item = db.query(UsersModel).filter(
            (UsersModel.username == userData["username"]) |
            (UsersModel.email == userData["email"])
        ).first()

        if not existing_item:
            # Enkripsi password menggunakan bcrypt
            userData["password"] = bcrypt.hash(default_password)

            # Buat instance UsersModel
            dbUser = UsersModel(**userData)
            db.add(dbUser)

    db.commit()
    print("Users seeded successfully!")
