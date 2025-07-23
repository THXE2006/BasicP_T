boss = 100

sword = 15
bow = 10
skill = 20

turn = 1

while True :
    level = input("เลือกโหมด easy , normal , hard :\n")
    if level == "easy" :
        level = 10
        print("คุณมีเวลา 10 เทิร์น")
        break
    elif level == "normal" :
        level = 7
        print("คุณมีเวลา 7 เทิร์น")
        break
    elif level == "hard" :
        level = 5
        print("คุณมีเวลา 5 เทิร์น")
        break
    else :
        print("เลือกระดับความยากอีกครั้ง")

player_name = input("Enter Your Name : ")
print("Welcome : " + player_name)
print("เจอมอนสะเต้อ เอาไงต่อดี")

while turn <= level + 1 :
    print("เทิร์นที่ :" + str(turn))
    
    if turn <= level :
        
        x = input("พิมพ์ [1 เพื่อต่อสู้] : [2 เพื่อหลบหนี]\n")

        if x == "1" or x == "2" :
            
            if x == "2" :
                print("หลบหนีสำเร็จ เร็จ เร็จ")
                break

            if boss > 0 or boss < 0 :
                if boss < 0 :
                    boss += 20
                    print("เลือดบอสฟื้นฟูขึ้นมา 20 หน่วย")

                if x == "1" :
                    print("เลือกอาวุธให้คิริตู่ ใส่เป็นตัวเลข")
                    weapon = input("[1 sword , 2 bow , 3 skill] :\n")
                    
                    if weapon == "1" :
                        turn += 1
                        boss -= sword
                        print("มอนเตอร์เลือดลดไป " + str(sword) + " แต้ม" + "\n" + "เลือดมอนเตอร์เหลือ : " + str(boss) + " แต้ม")
                        if boss == 0 :
                            print("YOU WIN!!!")
                            break
                    elif weapon == "2" :
                        turn += 1
                        boss -= bow
                        print("มอนเตอร์เลือดลดไป " + str(bow) + " แต้ม" + "\n" + "เลือดมอนเตอร์เหลือ : " + str(boss) + " แต้ม")    
                        if boss == 0 :
                            print("YOU WIN!!!")
                            break
                    elif weapon == "3" :
                        turn += 1
                        boss -= skill
                        print("มอนเตอร์เลือดลดไป " + str(skill) + " แต้ม" + "\n" + "เลือดมอนเตอร์เหลือ : " + str(boss) + " แต้ม")
                        if boss == 0 :
                            print("YOU WIN!!!")
                            break
                    else :
                        print("ErRoR เลือกอาวุธใหม่")
        else :
            print("เลือกใหม่อีกทีนะคิริตู่")
    else :
        if boss > 0 :
            print("YOU LOSE!! จบเกม คิริตู่โดนมอนตีตาย")
        break
    
    #ยังแสดงข้อความจบเกมไม่ได้