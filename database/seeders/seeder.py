from sqlalchemy.orm import Session
from config.connection import SessionLocal
from database.seeders.authorsSeeder import seedAuthors
from database.seeders.booksSeeder import seedBooks
from database.seeders.usersSeeder import seedUsers

def run_seeders():
    db: Session = SessionLocal()
    try:
        # Jalankan seeder untuk setiap tabel
        seedUsers(db)
        seedAuthors(db)
        seedBooks(db)
    finally:
        db.close()

if __name__ == "__main__":
    run_seeders()
