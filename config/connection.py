from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from config.app import settings

# env value database
dbConnection = settings.DB_CONNECTION
dbHost = settings.DB_HOST
dbPort = settings.DB_PORT
dbName = settings.DB_DATABASE
dbUsername = settings.DB_USERNAME
dbPassword = settings.DB_PASSWORD

# Membangun URL koneksi berdasarkan jenis DBMS
def get_database_url():
    if dbConnection == "sqlite":
        return f"sqlite:///./{dbName}.db"
    elif dbConnection == "mysql":
        return f"mysql+pymysql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}"
    elif dbConnection == "postgresql": 
        return f"postgresql://{dbUsername}:{dbPassword}@{dbHost}:{dbPort}/{dbName}"
    else:
        raise ValueError("Unsupported DB_CONNECTION in .env file")

DATABASE_URL = get_database_url()

# Debugging: Cek URL koneksi
print(f"Connecting to database using URL: {DATABASE_URL}")

# Membuat engine koneksi ke database
engine = create_engine(
    DATABASE_URL  # Untuk PostgreSQL, tidak memerlukan `connect_args`
)

# Coba koneksi ke database untuk validasi
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")

# Membuat session untuk operasi database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk model SQLAlchemy
Base = declarative_base()
