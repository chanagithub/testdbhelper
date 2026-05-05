import ui
import db_helper

def setup_view():
    # 1. เรียกข้อมูลจากฐานข้อมูล
    # ดึงรายชื่อ symbol ที่ไม่ซ้ำจากตาราง lots ในไฟล์ stocksbi2569.db  test for iphone
    dropdown_items = db_helper.get_unique_list('stocksbi2569.db', 'lots', 'symbol')

    # 2. สร้างหน้าจอหลัก (Main View)
    v = ui.View()
    v.name = 'Stock List'
    v.background_color = '#f0f0f7' # เปลี่ยนสีพื้นหลังให้อ่อนลงเล็กน้อยเพื่อให้ดูสบายตา

    # 3. สร้าง TableView เพื่อแสดงรายการ
    table = ui.TableView()
    
    # --- แก้ไขจุดนี้เพื่อให้เต็มจอ ---
    table.frame = v.bounds   # ให้ขนาดเริ่มต้นเท่ากับพื้นที่ของหน้าจอหลัก
    table.flex = 'WH'        # W = Width, H = Height (ยืดเต็มทั้งกว้างและสูงอัตโนมัติ)
    # ----------------------------
    
    # ตั้งค่าข้อมูลให้กับ TableView
    data_source = ui.ListDataSource(dropdown_items)
    table.data_source = data_source
    table.delegate = data_source
    
    # ฟังก์ชันเมื่อมีการจิ้มเลือกรายการ
    def item_selected(sender):
        if sender.selected_row >= 0:
            selected_item = sender.items[sender.selected_row]
            print(f'คุณเลือก: {selected_item}')

    data_source.action = item_selected
    
    # เพิ่มตารางเข้าไปในหน้าจอหลัก
    v.add_subview(table)
    
    # สั่งให้แสดงผลแบบเต็มจอ
    v.present('fullscreen')

if __name__ == '__main__':
    setup_view()
