import pyautogui
import time

def totugeki():
    print("totugekiに来たよ。")
    time.sleep(2)
    if pyautogui.locateCenterOnScreen("./mob2-2.png",grayscale = True,confidence=0.9):
            print("広い艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-2.png",grayscale = True,confidence=0.9)
            pyautogui.click(x,y)
            del x,y
            time.sleep(0.5)
            return totugeki2()
    elif pyautogui.locateCenterOnScreen("./mob2-2-1.png",grayscale = True,confidence=0.9):
            print("広い艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-2-1.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki2()
    elif pyautogui.locateCenterOnScreen("./muri.png",grayscale = True,confidence=0.9):
            print("目標海域に辿りつけません。")
            x,y = pyautogui.locateCenterOnScreen("./muri.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki2()
    elif pyautogui.locateCenterOnScreen("./muri2.png",grayscale = True,confidence=0.9):
            print("目標海域に辿りつけません。")
            x,y = pyautogui.locateCenterOnScreen("./muri2.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki2()
    elif pyautogui.locateCenterOnScreen("./kane.png",grayscale = True,confidence=0.9):
            print("kane艦隊")
            x,y = pyautogui.locateCenterOnScreen("./kane.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki()
    elif pyautogui.locateCenterOnScreen("./mob2-3-1.png",grayscale = True,confidence=0.9):
            print("黒い艦隊-1")
            x,y = pyautogui.locateCenterOnScreen("./mob2-3-1.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki()
    elif pyautogui.locateCenterOnScreen("./mob2-3.png",grayscale = True,confidence=0.9):
            print("黒い艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-3.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki()
    elif pyautogui.locateCenterOnScreen("./mob2-3-3.png",grayscale = True,confidence=0.9):
            print("黒い艦隊-3")
            x,y = pyautogui.locateCenterOnScreen("./mob2-3-3.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki()
    elif pyautogui.locateCenterOnScreen("./mob2-3-2.png",grayscale = True,confidence=0.9):
        print("黒い艦隊")
        x,y = pyautogui.locateCenterOnScreen("./mob2-3-2.png",grayscale = True,confidence=0.9)
        time.sleep(2)
        pyautogui.click(x,y)
        del x,y
        time.sleep(3)
        return totugeki()
    elif pyautogui.locateCenterOnScreen("./mob2-1.png",grayscale = True,confidence=0.9):
            print("小さい艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-1.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
            return totugeki()
    else:
        return main()
    time.sleep(2)
    if pyautogui.locateCenterOnScreen("./muri.png",grayscale = True ,confidence = 0.9 ):
        print("終了します")
        totugeki2()

def totugeki2():
    print("totugeki　2　に来たよ")
    time.sleep(5)
    if pyautogui.locateCenterOnScreen("./kane.png",grayscale = True,confidence=0.9):
        print("kane艦隊")
        x,y = pyautogui.locateCenterOnScreen("./kane.png",grayscale = True,confidence=0.9)
        time.sleep(2)
        pyautogui.click(x,y)
        del x,y
        time.sleep(3)
        return totugeki()
    elif pyautogui.locateCenterOnScreen("./muri.png",grayscale = True,confidence=0.9):
        print("目標海域に辿りつけません。")
        x,y = pyautogui.locateCenterOnScreen("./muri.png",grayscale = True,confidence=0.9)
        time.sleep(2)
        pyautogui.click(x,y)
        del x,y
        time.sleep(3)
        return totugeki3() 
    elif pyautogui.locateCenterOnScreen("./mob2-3.png",grayscale = True,confidence=0.9):
        print("黒い艦隊")
        x,y = pyautogui.locateCenterOnScreen("./mob2-3.png",grayscale = True,confidence=0.9)
        time.sleep(2)
        pyautogui.click(x,y)
        del x,y
        time.sleep(3)
        return totugeki()
    elif pyautogui.locateCenterOnScreen("./mob2-3-2.png",grayscale = True,confidence=0.9):
        print("黒い艦隊")
        x,y = pyautogui.locateCenterOnScreen("./mob2-3-2.png",grayscale = True,confidence=0.9)
        time.sleep(2)
        pyautogui.click(x,y)
        del x,y
        time.sleep(3)
        return totugeki()
    elif pyautogui.locateCenterOnScreen("./mob2-1.png",grayscale = True,confidence=0.9):
        print("小さい艦隊")
        x,y = pyautogui.locateCenterOnScreen("./mob2-1.png",grayscale = True,confidence=0.9)
        time.sleep(2)
        pyautogui.click(x,y)
        del x,y
        time.sleep(3)
        return totugeki()
    else:
        return main()
def totugeki3():
    print("totugeki　3　に来たよ")
    exit()

    
def main():
    print("開始")
    while True:
        x,y = (0,0)
        if pyautogui.locateCenterOnScreen("./stage2-1.png",grayscale=True,confidence = 0.9):
            print("ステージ選択")
            x,y = pyautogui.locateCenterOnScreen("./stage2-1.png",grayscale = True, confidence = 0.9)
            pyautogui.click(x,y)
            time.sleep(2)
            del x,y
        elif pyautogui.locateCenterOnScreen("./sortie.png",grayscale = True,confidence=0.9):
            print("出撃")
            x,y = pyautogui.locateCenterOnScreen("./sortie.png",grayscale = True,confidence=0.9)
            pyautogui.click(x,y)
            time.sleep(2)
            del x,y
        elif pyautogui.locateCenterOnScreen("./sortie2.png",grayscale = True,confidence=0.9):
            print("出撃へ")
            x,y = pyautogui.locateCenterOnScreen("./sortie2.png",grayscale = True,confidence=0.9)
            pyautogui.click(x,y)
            time.sleep(5)
            del x,y
        #目標海域には辿り着けません。
        elif pyautogui.locateCenterOnScreen("./muri.png",grayscale = True ,confidence = 0.9 ):
            print("目標海域にはたどり着けません。")
            time.sleep(1)
            totugeki()
        elif pyautogui.locateCenterOnScreen("./return.png",grayscale = True,confidence=0.9):
            print("回避")
            x,y = pyautogui.locateCenterOnScreen("./return.png",grayscale = True,confidence=0.9)
            time.sleep(2)
            pyautogui.click(x,y)
            del x,y
            time.sleep(3)
        elif pyautogui.locateCenterOnScreen("./boss.png",grayscale = True,confidence=0.9):
            print("ボス")
            x,y = pyautogui.locateCenterOnScreen("./boss.png",grayscale = True,confidence=0.9)
            time.sleep(2)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
        elif pyautogui.locateCenterOnScreen("./mob2-2-1.png",grayscale = True,confidence=0.9):
            print("広い艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-2-1.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
        elif pyautogui.locateCenterOnScreen("./mob2-2.png",grayscale = True,confidence=0.9):
            print("広い艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-2.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
        elif pyautogui.locateCenterOnScreen("./mob2-2-2.png",grayscale = True,confidence=0.9):
            print("広い艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-2-2.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
        elif pyautogui.locateCenterOnScreen("./mob2-1.png",grayscale = True,confidence=0.9):
            print("主力艦隊")
            time.sleep(1)
            del x,y
            x,y = pyautogui.locateCenterOnScreen("./mob2-1.png",grayscale = True,confidence=0.9)
            time.sleep(1)
            pyautogui.click(x,y)
            del x,y
            time.sleep(1)
        elif pyautogui.locateCenterOnScreen("./mob2-3.png",grayscale = True,confidence=0.9):
            print("黒い艦隊")
            x,y = pyautogui.locateCenterOnScreen("./mob2-3.png",grayscale = True,confidence=0.9)
            time.sleep(2)
            pyautogui.click(x,y)
            del x,y
            time.sleep(3)
        #編成出撃画面
        elif pyautogui.locateCenterOnScreen("./sortie3.png",grayscale = True,confidence=0.9):
            print("出撃へ")
            x,y = pyautogui.locateCenterOnScreen("./sortie3.png",grayscale = True,confidence=0.9)
            time.sleep(2)
            pyautogui.click(x,y)
            del x,y
        #結果画面のタッチ操作
        elif pyautogui.locateCenterOnScreen("./touch.png",grayscale = True , confidence = 0.9):
            print("結果画面")
            x,y = pyautogui.locateCenterOnScreen("./touch.png",grayscale = True , confidence = 0.9)
            time.sleep(2)
            pyautogui.click(x,y)
            del x,y
        #アイテム入手
        elif pyautogui.locateCenterOnScreen("./item_touch.png",grayscale = True , confidence = 0.9):
            print("アイテム入手")
            x,y = pyautogui.locateCenterOnScreen("./item_touch.png",grayscale = True , confidence = 0.9)
            time.sleep(2)
            pyautogui.click(x,y)
            del x,y
        elif pyautogui.locateCenterOnScreen("./confirm.png",grayscale = True , confidence = 0.9):
            print("アイテム入手")
            x,y = pyautogui.locateCenterOnScreen("./confirm.png",grayscale = True , confidence = 0.9)
            time.sleep(2)
            pyautogui.click(x,y)
            del x,y
        else:
            print("wait")
            time.sleep(3)
            print("再探索")







if '__main__' == __name__:
    main()



