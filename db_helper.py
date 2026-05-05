import sqlite3

def get_unique_list(db_file, table_name, field_name):
    """
    ดึงข้อมูลจาก sqlite โดยคัดเลือกเฉพาะค่าที่ไม่ซ้ำกัน
    """
    items = []
    try:
        # เชื่อมต่อฐานข้อมูล
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # ใช้ SELECT DISTINCT เพื่อดึงข้อมูลที่ไม่ซ้ำ
        query = f"SELECT DISTINCT {field_name} FROM {table_name} WHERE {field_name} IS NOT NULL ORDER BY {field_name}"
        cursor.execute(query)
        
        # ดึงข้อมูลทั้งหมดและแปลงจาก tuple เป็น list ปกติ
        items = [row[0] for row in cursor.fetchall()]
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
    return items