from app.database.db import engine

try:
    conn = engine.connect()
    print("Database Connected")
    conn.close()

except Exception as e:
    print(e)
