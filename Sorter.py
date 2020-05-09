import subprocess
from pathlib import Path
import os

liste = list()
listenumbs = list()
listenumsb = list()
while True:
    subprocess.Popen("cls", shell=True).communicate()
    print("""
    1] Word Sorting
    2] Number Sorting
    3] Help
    4] Exit
    """)
    y = input(">>>> ")

    if y == "1":
        while True:
            subprocess.Popen("cls", shell=True).communicate()
            print("List: " + str(liste))
            x = input("Enter word here: ")
            liste.append(x)
            liste.sort()
            print(liste)
            print("Do you want to continue: " + "\n1] Yes" + "\n2] No" + "\n3] Delete from list")
            c = input(">>>> ")
            if c == "1":
                continue
            elif c == "2":
                print("Do you want to save file?" + "\n1] Yes" + "2] No")
                ans = input(">>>> ")
                if ans == "1":
                    home = str(Path.home())
                    path = os.path.join(home, "Desktop\\WordSorting.txt")
                    with open(path, "w+") as f:
                        f.write("Your List" + "\n" + str(liste))
                        print("Saved to your Desktop!")
                elif ans == "2":
                    break;
            elif c == "3":
                subprocess.Popen("cls", shell=True).communicate()
                print("List" + str(liste))
                delete = input("Enter the index number (Starts from 0): ")
                liste.pop(int(delete))
                print("List: " + str(list))
                oylesine = input("Press space to continue...")
                continue

    elif y == "2":
        while True:
            subprocess.Popen("cls", shell=True).communicate()
            print("List Small-Big: " + str(listenumbs))
            print("List Big-Small: " + str(listenumsb))
            v = float(input("Enter number here: "))
            listenumbs.append(v)
            listenumsb.append(v)
            listenumbs.sort()
            listenumsb.sort(reverse = True)
            print(listenumbs)
            print(listenumsb)
            print("Do you want to continue: " + "\n1] Yes" + "\n2] No" + "\n3] Delete from list")
            c = input(">>>> ")
            if c == "1":
                continue
            elif c == "2":
                print("Do you want to save file?" + "\n1] Yes" + "\n2] No")
                ans = input(">>>> ")
                if ans == "1":
                    home = str(Path.home())
                    path = os.path.join(home, "Desktop\\NumberSorting.txt")
                    with open(path, "w+") as f:
                        f.write("Your List Big-Small" + "\n" + str(listenumsb))
                        f.write("\nYour List Small-Big" + "\n" + str(listenumbs))
                        print("Saved to your Desktop!")
                        break;
                elif ans == "2":
                    break;
            elif c == "3":
                subprocess.Popen("cls", shell=True).communicate()
                listenumbs.pop()
                listenumsb.pop()
                print("List Big-Small" + str(listenumbs))
                deletebs = input("Enter the index number (Starts from 0): ")
                print("List Small-Big" + str(listenumsb))
                deletesb = input("Enter the index number (Starts from 0): ")
                listenumbs.pop(int(deletebs))
                listenumsb.pop(int(deletesb))
                print("List: " + str(listenumbs))
                print("List: " + str(listenumsb))
                gec = input("Press space to continue...")
                continue
            
    elif y == "3":
        print("""
        This application helps you to sort any numbers and any string. You can save files to your desktop under the name of "WordSorting.txt" or "NumberSorting.txt".
        Have fun...
        """)
        go = input("Press space to continue...")
        continue
    elif y == "4":
        break;