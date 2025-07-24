# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    # TODO: วนลูปแสดงชื่อหนังพร้อมราคาตั๋ว
    for movie in movie_list :
        print(f"ชื่อหนัง : {movie['movie_name']} | ราคาตั๋ว : {movie['ticket_price']} บาท")

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    if age_restriction == 'G' :
        return True
    elif user_age > age_restriction :
        return True
    else :
        print("อายุน้อยเกินไปนะน้อง Too Youg น่ะ")
        return False

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Horror' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม
    if genre == 'Horror' :
        base_price += 50
        return base_price
    else :
        return base_price

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    # TODO: 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    # 3. รับอายุผู้ใช้
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
    show_movies(movie_list)
    choose = int(input("ระบุเรื่องที่ต้องการดู (1-5) : ")) - 1
    age = input("กรุณากรอกอายุ : ")
    if check_age(age , movie_list[choose]['age_restriction']) == False :
        return
    while True :
        soundtrack = input("กรุณาเลือกเสียงพากย์ [1 = พากย์ไทย] [2 = Soundtrack]\n")
        if soundtrack == "1" :
            soundtrack = "พากย์ไทย"
            break
        elif soundtrack == "2" :
            soundtrack = "Soundtrack"
            break
        else :
            print("กรุณาเลือกให้ถูกต้อง")
    print(f"ผลการซื้อตั๋วหนัง เรื่อง : {movie_list[choose]['movie_name']} | {soundtrack} {calculate_price(movie_list[choose]['ticket_price'],movie_list[choose]['genre'])} บาท")

def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด
    # 2. ซื้อตั๋วหนัง

    print("1.แสดงหนังทั้งหมด\n2.ซื้อตั๋วหนัง\n[โปรดเลือกรายการ]")

    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = input("เลือกเมนู: ")

    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง
    if menu == "1" :
        show_movies(movies)
        main()
    elif menu == "2" :
        buy_ticket(movies)
    else :
        print("เลือกเมนูใหม่อีกครั้ง")
        main()

# เรียก main เพื่อเริ่มโปรแกรม
main()