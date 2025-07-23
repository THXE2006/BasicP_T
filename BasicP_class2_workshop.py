x = int(input("กรอกระยะทางเป็นจำนวนเต็ม : "))

if x < 0 :
    print("ไม่ตลก อย่าชีวิตติดลบ")
    x = x * -1
    print("ระยะทางใหม่ : " + str(x) + '\n')
elif x == 0 :
    print("เดินมาก็ได้มั้ง" + '\n')

def func(distance) :
    print("ระยะทาง : " + str(distance))

if 5 <= x <= 50 :
    func(x)
    print("ค่าส่ง 10 บาท")
elif 51 <= x <= 100 :
    func(x)
    print("ค่าส่ง 15 บาท")
elif 101 <= x <= 300 :
    func(x)
    print("ค่าส่ง 25 บาท")
elif 301 <= x <= 500 :
    func(x)
    print("ค่าส่ง 35 บาท")
elif 501 <= x :
    func(x)
    print("ค่าส่ง 45 บาท")
else :
    func(x)
    print("ส่งฟรีใส่Code : IHAVECPU ด้วยนะจ๊ะ")