from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

try:
    engine = create_engine(os.getenv("DATABASE_URL"))
    connection = engine.connect()
    print("✅ Database connected successfully!")
    connection.close()
except Exception as e:
    print(f"❌ Error: {e}")
    