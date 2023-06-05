import time
import os

print("Welcome to the TuxBuilder CLI!")

time.sleep(1)

print("\n")
print("This tool will help you build the Super Mario 64 PC Port on Linux without fuss!")

def dependencies():
    distropkgmgr = input('''Which package manager does your distribution use?
    1. APT (Debian, Ubuntu , Zorin OS, elementary, Linux Mint, Pop!_OS and the other 1920839840938290 Ubuntu-based distros)
    2. Pacman (Arch, Manjaro, EndeavourOS, Garuda etc.)
    3. XBPS-install (Void Linux)
    4. DNF (Fedora)
    5. "      " (slackware) 
    --->  ''')
    if distropkgmgr == "APT" or "apt" or "1":
        os.system("sudo apt install build-essential git python3 libglew-dev libsdl2-dev curl libcurl4-gnutls-dev libjsoncpp-dev")
    elif distropkgmgr == "Pacman" or "pacman" or "2":
        os.system("sudo pacman -S base-devel python sdl2 glew curl")
    elif distropkgmgr == "XBPS" or "xbps" or "XBPS-install" or "xbps-install":
        os.system("sudo xbps-install -S base-devel git curl python3 SDL2-devel glew-devel")
    elif distropkgmgr == "DNF" or "dnf":
        os.system("sudo dnf install make gcc python3 glew-devel SDL2-devel")
    elif distropkgmgr == "slackware" or "      ":
        print(":[ sorry")
    else:
        print("Invalid")

dependencies()

def reposelect():
    global repo
    print("\n")
    repo = input('''What repository will you be building today? \n
    You have a choice of:
    1. Render96ex (alpha, master, tester, tester_rt64alpha)
    2. SM64ex (nightly, master, coop, alo and more to come!)
    3. SM64rt (master, fsr)
    4. Custom repository (not recommended) 
    5. Saturn (best for Machinima-making purposes) (only legacy Saturn)
    So, what will it be? Choose the number stated before the repository name.    ''')

reposelect()

def render96sel():
    confirmation = input("\nYou have selected Render96ex. After the confirmation, you will be asked to select which branch to use. Input yes or no BUT do not enter Y or N.  ")
    if confirmation == "yes":
        branchren96 = input('''Which branch to clone and build? \n
        1. Master (old, outdated)
        2. Alpha (best choice for regular players)
        3. Tester (bleeding edge features and bugfixes)
        4. Tester_RT64Alpha (make sure you have a good enough GPU and drivers for this! As Linus Torvalds once said, "(expletive) you, NVIDIA"!) \n''')
        if branchren96 == "1":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/Render96/Render96ex --branch master")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("Render96ex")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("Render96ex")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("Render96ex")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("Render96ex")
                os.system("make -j8")
        elif branchren96 == "2":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/Render96/Render96ex --branch alpha")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("Render96ex")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("Render96ex")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("Render96ex")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("Render96ex")
                os.system("make -j8")
        elif branchren96 == "3":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/Render96/Render96ex --branch tester")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("Render96ex")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("Render96ex")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("Render96ex")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("Render96ex")
                os.system("make -j8")
        elif branchren96 == "4":
            print("Put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            pleaseconfirm = input("WARNING! Are you sure that you want to clone the tester RT64 BRANCH? It won't be fun if you don't have a decent GPU! ")
            if pleaseconfirm == "yes":
                print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!")
                time.sleep(3)
                os.system("git clone https://github.com/Render96/Render96ex --branch tester_rt64alpha")
                print("Copying baserom....")
                os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
                print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("Render96ex")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("Render96ex")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("Render96ex")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("Render96ex")
                os.system("make -j8")
            elif pleaseconfirm == "no":
                render96sel()
    elif confirmation == "no":
        reposelect()

def sm64exsel():
    smexconf = input("\n You have selected SM64EX. You will be asked to select which branch to use after the confirmation. Input yes or no! (NOT y or n) ")
    if smexconf == "yes":
        branchsmex = input('''Which branch to clone and build? \n
        1. Nightly (recommended)
        2. Master (alright, I guess)
        3. Coop (play with friends! I built this branch myself, now all I need are friends! :DDD... oh wait-)
        4. Alo (Honestly don't know what the difference is, but I'm sure it's good!)
        5. There are WAYYY too many SM64ex branches. This is only an alpha build. More to come! ''')
        if branchsmex == "1":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/sm64pc/sm64ex --branch nightly")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("sm64ex")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("sm64ex")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("sm64ex")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("sm64ex")
                os.system("make -j8")
        elif branchsmex == "2":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/sm64pc/sm64ex --branch master")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex/baserom.us.z64")
            print("Baserom copied!")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("sm64ex")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("sm64ex")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("sm64ex")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("sm64ex")
                os.system("make -j8")
        elif branchsmex == "3":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!")
            time.sleep(3)
            os.system("git clone https://github.com/djoslin0/sm64ex-coop")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex-coop/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("sm64ex-coop")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("sm64ex-coop")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("sm64ex-coop")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("sm64ex-coop")
                os.system("make -j8")
        elif branchsmex == "4":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/AloXado320/sm64ex-alo")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex-alo/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("sm64ex-alo")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("sm64ex-alo")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("sm64ex-alo")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("sm64ex-alo")
                os.system("make -j8")
    elif smexconf == "no":
        reposelect()

def sm64rtsel():
    sm64rtconf = input("You have selected SM64RT. You will be asked to select which branch to clone after the confirmation. Input yes or no! (NOT y or n) ")
    if sm64rtconf == "yes":
        branchsm64rt = input('''You have selected SM64RT. Here are the two available branches:
        1. Master (what you should normally use)
        2. fsr (can anyone tell me the difference?)''')
        if branchsm64rt == "1":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/DarioSamo/sm64rt --branch master")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64rt/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("sm64rt")
                os.system("make -j2 RENDER_API=RT64 EXTERNAL_DATA=1")
            elif buildspeed1 == "2":
                os.chdir("sm64rt")
                os.system("make -j4 RENDER_API=RT64 EXTERNAL_DATA=1")
            elif buildspeed1 == "3":
                os.chdir("sm64rt")
                os.system("make -j6 RENDER_API=RT64 EXTERNAL_DATA=1")
            elif buildspeed1 == "4":
                os.chdir("sm64rt")
                os.system("make -j8 RENDER_API=RT64 EXTERNAL_DATA=1")
        elif branchsm64rt == "2":
            print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!\n")
            time.sleep(3)
            os.system("git clone https://github.com/DarioSamo/sm64rt --branch fsr")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64rt/baserom.us.z64")
            print("Baserom copied!\n")
            time.sleep(2)
            buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
            1. Slow (-j2)
            2, Normal (-j4)
            3. Faster than normal (-j6)
            4. Hyper (-j8) \n
            Select the number mentioned before ''')
            if buildspeed1 == "1":
                os.chdir("sm64rt")
                os.system("make -j2")
            elif buildspeed1 == "2":
                os.chdir("sm64rt")
                os.system("make -j4")
            elif buildspeed1 == "3":
                os.chdir("sm64rt")
                os.system("make -j6")
            elif buildspeed1 == "4":
                os.chdir("sm64rt")
                os.system("make -j8")

def customrepouse():
    whoopsiesmaybe = input("Are you sure you want to select a custom repository? You will have to manually copy the BaseROM to the folder. ")
    if whoopsiesmaybe == "yes":
        x = input("input the repo WITH  'git clone'! (e.g. git clone https://github.com/user-or-group/repository-name) ")
        print(x)
        time.sleep(1)
        os.system(x)
    elif whoopsiesmaybe == "no":
        reposelect()

def saturnsel():
    saturnconfirm = input("You have selected Saturn. Nifty little repository for copying SMG4- just kidding! Are you sure you want to select this repository? Input yes or no, but NOT y or n. ")
    if saturnconfirm == "yes":
        print("\nPLEASE put your Super Mario 64 ROM in your home folder and rename it to 'baserom.us.z64' without the quotes!")
        time.sleep(3)
        os.system("git clone https://github.com/Llennpie/Saturn --branch legacy")
        print("Copying baserom....")
        os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Saturn/baserom.us.z64")
        print("Baserom copied!")
        print("You will be asked to enter your Sudo password in a second. This is to fix an issue with building on Linux, where make spits out a 'No such file or disrectory' error about the file 'json/json.h'.")
        time.sleep(1)
        os.system("sudo ln -s /usr/include/jsoncpp/json/ /usr/include/json")
        time.sleep(2)
        buildspeed1 = input('''Now, it comes to building the game. How fast do you want the game to build?
        1. Slow (-j2)
        2, Normal (-j4)
        3. Faster than normal (-j6)
        4. Hyper (-j8) \n
        Select the number mentioned before ''')
        if buildspeed1 == "1":
            os.chdir("Saturn")
            os.system("make -j2")
        elif buildspeed1 == "2":
             os.chdir("Saturn")
             os.system("make -j4")
        elif buildspeed1 == "3":
            os.chdir("Saturn")
            os.system("make -j6")
        elif buildspeed1 == "4":
            os.chdir("Saturn")
            os.system("make -j8")
    elif saturnconfirm == "no":
        reposelect()


if repo == "1":
    render96sel()
elif repo == "2":
    sm64exsel()
elif repo == "3":
    sm64rtsel()
elif repo == "4":
    customrepouse()
elif repo == "5":
    saturnsel()
else:
    print("That was invalid. Try again and restart the script. \n")

print("If you encounter any problems in building, try again, and follow the instructions properly.")