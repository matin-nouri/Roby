import pyautogui as pag
from time import sleep
print("*** Record New Data ***")
conf = input("# Record Name : ")
data = ""

with open(f"{conf}.task","r+") as file:
    data = file.readlines()
    file.close()

count = 0
for i in data:
    count+=1

for i in range(0,count):
    step = data[i].replace("\n","")
    command = step.split(" ")
    if command[0] == "MP":
        vstep = data[i+1]
        vcommand = vstep.split(" ")
        x = int(command[1])
        y = int(command[2])
        if vcommand[0] == "DEL":
            pag.moveTo(x,y,int(vcommand[1]))
        else:
            pag.moveTo(x,y)
    elif command[0] == "DEL":
        vstep = data[i-1]
        vcommand = vstep.split(" ")
        if vcommand[0] == "MP":
            pass
        else:
            sleep(int(command[1]))
    elif command[0] == "LC":
        pag.click()
    elif command[0] == "MC":
        pag.middleClick()
    elif command[0] == "RC":
        pag.rightClick()
    elif command[0] == "KY":
        text = step.replace("KY ","")
        pag.typewrite(text,0.1)
    elif command[0] == "HK":
        vstep = step.replace("HK ","")
        vcommand = vstep.split(" ")
        pag.typewrite(vcommand)
    elif command[0] == "SC":
        unit = int(command[1])
        if command[2] == "down":
            unit *= -1
        pag.scroll(unit)
    elif command[0] == "DG":
        x = int(command[1])
        y = int(command[2])
        pag.drag(x,y,0.1)
    elif command[0] == "RL":
        vstep = data[i+1]
        vcommand = vstep.split(" ")
        x = int(command[1])
        y = int(command[2])
        if vcommand[0] == "DEL":
            pag.moveRel(x,y,int(vcommand[1]))
        else:
            pag.moveRel(x,y)
        