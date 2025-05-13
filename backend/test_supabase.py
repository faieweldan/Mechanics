from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")

print(f"SUPABASE_URL: {url}")

try:
    supabase = create_client(url, key)
    # Try to access auth to test connection
    print("✅ Supabase client created successfully!")
except Exception as e:
    print(f"❌ Error: {e}")