from pyautogui import *
import pyautogui
from PIL import ImageGrab
import time
import keyboard
import random
from pytesseract import *
pytesseract.tesseract_cmd = r"C:\Users\Admin\Desktop\Programing\PYTHON LOL BOT\Tesseract\tesseract.exe"

def cordsToText(x1,y1,x2,y2):
    im = ImageGrab.grab(bbox =(x1, y1, x2, y2))
    im = im.convert('L')
    text = pytesseract.image_to_string(im)
    return text
    

ItemList = [["Doran's Blade", 450],
    ["Long Sword", 350],
    ["Vampiric Scepter", 550],
    ["Long Sword", 350],
    ["Long Sword", 350],
    ["Dagger", 300],
    ["Noonquiver", 300],
    ["Cloak of Agility", 600],
    ["Immortal Shieldbow", 600]]



while True:
    time.sleep(2)
    if pyautogui.locateOnScreen("playButton.png",confidence=0.8) != None:
        print("Play Button found")
        time.sleep(2)
        print("CLICK: Play")
        pyautogui.click(426, 196)
        time.sleep(2)
        pyautogui.click(461, 259)
        time.sleep(2)
        pyautogui.click(737, 655)
        time.sleep(2)
        pyautogui.click(862, 842)
        time.sleep(2)
        pyautogui.click(862, 842)

    if pyautogui.locateOnScreen("acceptButton.png",confidence=0.8) != None:
            time.sleep(2)
            pyautogui.click(950, 708)
            
            
            
    if pyautogui.locateOnScreen("chooseYourChampion.png",confidence=0.8) != None:
            time.sleep(2)
            pyautogui.click(1137, 259)
            time.sleep(2)
            pyautogui.typewrite("ezreal", interval=0.5)
            time.sleep(2)
            pyautogui.click(703, 320)
            time.sleep(2)
            pyautogui.click(953, 765)
            
    if pyautogui.locateOnScreen("honorATeammate.png",confidence=0.8) != None:
        pyautogui.click(958, 810)
        time.sleep(2)
    
    if pyautogui.locateOnScreen("dailyPlay.png",confidence=0.8) != None:
        time.sleep(2)
        pyautogui.click(961, 549)
        time.sleep(2)
        pyautogui.click(965, 835)
        
            
    if pyautogui.locateOnScreen("prepareForBattle.png",confidence=0.8) != None:
        while pyautogui.locateOnScreen("uppgradeButton.png",confidence=0.8) == None:
            time.sleep(2)
        gameRunning = True
        Item = 0
        while gameRunning:
            time.sleep(0.2)
            HP = cordsToText(846, 1027, 935, 1045)
            HP = HP.split("/")
            HP[0] = int(HP[0])
            HP[1] = int(HP[1])
            HP = HP[1] / HP[0]
            print(HP)
            Money = int(cordsToText(1200, 1046, 1276, 1068))
            if pyautogui.locateOnScreen("uppgradeButton.png",confidence=0.8) != None:
                print("LVL")
                pyautogui.hotkey("ctrl","r")
                pyautogui.hotkey("ctrl","q")
                pyautogui.hotkey("ctrl","w")
                pyautogui.hotkey("ctrl","e")

            if HP > 0.8:
                pyautogui.click(1282, 372,1,"right")
                
            if HP < 0.4:
                pyautogui.click(1753, 966,1,"right")
                time.sleep(10)
                pyautogui.write("b")
                time.sleep(10)
                if Item < len(ItemList):
                    while Money > ItemList[Item][1]:
                        time.sleep(2)
                        pyautogui.write("p")
                        time.sleep(2)
                        pyautogui.hotkey("ctrl","l")
                        time.sleep(2)
                        pyautogui.write(ItemList[Item][0])
                        time.sleep(2)
                        pyautogui.click(295, 360,1,"right")
                        time.sleep(2)
                        pyautogui.write("p")
                        time.sleep(2)
                        Money = int(cordsToText(1200, 1046, 1276, 1068))

                    
                    
                
            
            #ENEMYS
            if HP > 0.4:
                ePos = pyautogui.locateOnScreen("redMinion1",confidence=0.8)
                if ePos != None:
                    x = ePos.left + ePos.width/2
                    y = ePos.Top + ePos.height/2
                    pyautogui.click(x,y,1,"right")
                    pyautogui.write("q")
                    pyautogui.write("w")

                ePos = pyautogui.locateOnScreen("redMinion2",confidence=0.8)
                if ePos != None:
                    x = ePos.left + ePos.width/2
                    y = ePos.Top + ePos.height/2
                    pyautogui.click(x,y,1,"right")
                    pyautogui.write("q")
                    pyautogui.write("w")

                ePos = pyautogui.locateOnScreen("redMinion3",confidence=0.8)
                if ePos != None:
                    x = ePos.left + ePos.width/2
                    y = ePos.Top + ePos.height/2
                    pyautogui.click(x,y,1,"right")
                    pyautogui.write("q")
                    pyautogui.write("w")
                
            
        
            



#DAILY PLAY
        #(961, 549)
        #(965, 835)

#EXIT END LOBBY
        #(767, 843)

#BUY LIST
#CTLR+L = SERCH
#Dorans blade
#Imortal sheild bow

#Ability CTRL+ R Q W E

#HP TOPLEFT (846, 1027)
#HP BOTTOMRIGHT (935, 1045)
#MONEY TOPLEFT (1200, 1046)
#MONEY BOTTOMRIGHT (1276, 1068)
#SAFE SPOT (1753, 966)
#Buy Item spot (295, 360)
#SKIP HONOR (958, 810)
#LEVEL UP OK 
#HP 0-100%






#ATT GÖRA. (VICTORY/DEFEAT SCREEN)
#ATT GÖRA. ENEMY TURRETS ALIVE

