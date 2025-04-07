from supabase import create_client, Client

SUPABASE_URL = "https://igdyolghmogpjmjlpzgs.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlnZHlvbGdobW9ncGptamxwemdzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM5OTQwNTUsImV4cCI6MjA1OTU3MDA1NX0.Z7ek0HjEOkZ-4heMSzrfMCDoUBg9M7mpS6vE504bgPc"

def conectar_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)
