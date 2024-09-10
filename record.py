import pyautogui as pag
print("*** Record New Data ***")
conf = input("# Record Name : ")
with open(f"{conf}.task","w+") as file:
    data= ""
    while True:
        print("""Choose One of the below options:
                1) Mouse Point
                2) Move Mouse
                3) Mouse Click
                4) Mouse Scroll
                5) Mouse Drag
                6) Keyboard String
                7) Keyboard Hotkey
                8) Delay in Second
                9) Finish""")
        act = int(input("> "))
        assert act <= 9
        if act == 1:
            x = 0
            y = 0
            print("Whenever your mouse point is okay, press Ctrl + C.")
            try:
                while True:
                    x = pag.position().x
                    y = pag.position().y
                    print(f"Your Mouse Point : {x} {y}",end="\r")
            except:
                pass    
            data+=f"MP {x} {y}\n"
            print(f"Mouse Point {x} {y} has been recorded.")
        elif act==2:
            print("e.g. 400 0, 0 100, 100 100")
            i = input("> ")
            data+=f"RL {i}\n"
            print(f"{i} has been recorded.")
        elif act==3:
            print("1. Left | 2. Middle | 3. Right")
            i = int(input("> "))
            if i == 1:
                data+=f"LC\n"
                print("Left Click has been recorded.")
            elif i ==2:
                data+=f"MC\n"
                print("Middle Click has been recorded.")
            elif i ==3:
                data+=f"RC\n"
                print("Right Click has been recorded.")
        elif act==4:
            print("e.g. : 20 up , 40 down")
            i = input("> ")
            data+=f"SC {i}\n"
            print(f"{i} has been recorded.")
        elif act==5:
            print("e.g. 400 0, 0 100, 100 100")
            i = input("> ")
            data+=f"DG {i}\n"
            print(f"{i} has been recorded.")
        elif act==6:
            print("Keyboard: ")
            i = input("> ")
            data+=f"KY {i}\n"
            print(f"{i} has been recorded.")
        elif act==7:
            print("Write in this template: ctrl r")
            i = input("> ")
            data+=f"HK {i}\n"
            print(f"{i} has been recorded.")
        elif act==8:
            print("Delay in Second: ")
            i = input("> ")
            data+=f"DEL {i}\n"
            print(f"{i} has been recorded.")
        elif act==9:
            break
    file.writelines(data)
    file.close()