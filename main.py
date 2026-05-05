import ui
import db_helper

def setup_view():
    # 1. เรียกข้อมูลจากโมดูล (ระบุชื่อไฟล์, ตาราง, และฟิลด์)
    # สมมติว่าไฟล์ชื่อ data.sqlite ตารางชื่อ products ฟิลด์ชื่อ category. this is test for iSH
    dropdown_items = db_helper.get_unique_list('data.sqlite', 'products', 'category')

    # 2. สร้างหน้าจอ UI
    v = ui.View()
    v.name = 'Dropdown Example'
    v.background_color = 'white'

    # 3. สร้าง TableView เพื่อทำหน้าที่เป็นรายการเลือก
    table = ui.TableView()
    table.frame = (10, 10, 300, 200)
    
    # นำข้อมูลที่ได้จาก sqlite มาใส่ใน DataSource
    data_source = ui.ListDataSource(dropdown_items)
    table.data_source = data_source
    table.delegate = data_source
    
    # ฟังก์ชันเมื่อมีการเลือกรายการ
    def item_selected(sender):
        selected_item = sender.items[sender.selected_row]
        print(f'คุณเลือก: {selected_item}')

    data_source.action = item_selected
    
    v.add_subview(table)
    v.present('sheet')

if __name__ == '__main__':
    setup_view()
