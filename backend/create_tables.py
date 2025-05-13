from sqlalchemy import create_engine
from models import Base
from dotenv import load_dotenv
import os

load_dotenv()

# Create engine
engine = create_engine(os.getenv("DATABASE_URL"))

# Create all tables
try:
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully!")
except Exception as e:
    print(f"❌ Error creating tables: {e}")