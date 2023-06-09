import time
import colorama
from colorama import Fore, Back, Style
import os
colorama.init(autoreset=True)

print(f"{Fore.RED}RED text means important information.")
print(f"{Fore.GREEN}GREEN text means general comments.")
print(f"{Fore.BLUE}BLUE text indicates user input.\n")
time.sleep(2)

print(f"{Fore.GREEN}TuxBuilderCLI: A tool to easily build the SM64 PC Port without fuss. \n")


def dependencies():
    distropkgmgr = input(f'''{Fore.CYAN}Select your distribution's package manager-\n
    1. APT (Debian, Ubuntu , Zorin OS, elementaryOS, Linux Mint, Pop!_OS and the other bajillion Ubuntu-based distros)
    2. Pacman (Arch, Manjaro, EndeavourOS, Garuda, blendOS, pearOS Nicec0re etc.)
    3. XBPS-install (Void Linux)
    4. DNF (Fedora, Nobara, RisiOS etc.) 
    5. Skip (Select if you have already installed the dependencies for your distribution.)
    --->  ''')
    if distropkgmgr == "1":
        os.system("sudo apt install build-essential git python3 libglew-dev libsdl2-dev curl libcurl4-gnutls-dev libjsoncpp-dev")
    elif distropkgmgr == "2":
        os.system("sudo pacman -S base-devel python sdl2 glew curl")
    elif distropkgmgr == "3":
        os.system("sudo xbps-install -S base-devel git curl python3 SDL2-devel glew-devel")
    elif distropkgmgr == "4":
        os.system("sudo dnf install make gcc python3 glew-devel SDL2-devel")
    elif distropkgmgr == "5":
        p = input(f"{Fore.BLUE}Have you installed the dependencies for your distribution yet? (y,n) ")
        if p == "y":
            print("Noted. Skipping...")
            time.sleep(2)
        elif p == "n":
            print("Gotcha. Reverting back to dependency manager.")
            dependencies()

dependencies()

time.sleep(1)
print("Building the game requires a baserom to extract assets from. If you don't have a baserom yet, obtain one now.")
time.sleep(2)
def bromobtain():
    brom = input("Have you obtained a baserom yet? (y,n)")
    if brom == "y":
        print("Fantastic. Place the baserom in your home folder and rename it to 'baserom.us.z64'. Don't worry, I won't ask where it came from ;) ")
        dependencies()
    elif brom == "n":
        print("The script will loop this question until you have obtained your baserom.")
        time.sleep(2)
        return bromobtain()
    time.sleep(3)


def reposelect():
    global repo
    repo = input('''Select the repository you would like to build today. - \n
    You have a choice of:
    1. Render96ex (alpha, master, tester, tester_rt64alpha)
    2. SM64ex (nightly, master, coop, alo and more to come!)
    3. SM64rt (master, fsr)
    4. Saturn (best for Machinima-making purposes) (only legacy Saturn)
    So, what will it be? Choose the number stated before the repository name.    ''')

reposelect()

def render96sel():
    print(f"\n{Fore.GREEN}You have selected Render96ex.")
    confirmation = input(f"\n{Fore.BLUE}Is the above selection correct? (y,n) ")
    if confirmation == "y":
        branchren96 = input(f'''\n{Fore.BLUE}Select the branch to be built. (Render96ex) \n
        1. Master (old, outdated)
        2. Alpha (best choice for regular players)
        3. Tester (bleeding edge features and bugfixes)
        4. Tester_RT64Alpha (Don't use if your GPU doesn't support Ray Tracing. If it does don't use open-source drivers, like Nouveau.) \n''')
        if branchren96 == "1":
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/Render96/Render96ex --branch master")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
            print("Baserom copied, ready for building.\n")
            time.sleep(2)
            buildspeed1 = input(f'''\n{Fore.BLUE}The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/Render96/Render96ex --branch alpha")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
            print("Baserom copied.\n")
            time.sleep(2)
            buildspeed1 = input(f'''{Fore.BLUE}The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/Render96/Render96ex --branch tester")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
            print("Baserom copied.\n")
            time.sleep(2)
            buildspeed1 = input(f'''{Fore.BLUE}The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            pleaseconfirm = input(f"{Fore.RED}|WARNING| You have selected the RT64 branch. Is this correct?  ")
            if pleaseconfirm == "y":
                print("\nConfirm you have copied baserom.us.z64 to your home folder.")
                time.sleep(3)
                os.system("git clone https://github.com/Render96/Render96ex --branch tester_rt64alpha")
                print("Copying baserom....")
                os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Render96ex/baserom.us.z64")
                print("Baserom copied.\n")
            elif pleaseconfirm == "n":
                print("THat was almost a disaster. Reverting back to Render96ex branch selection...")
                render96sel()
            else:
                print("Invalid option. Reverting back to Render96ex branch selection.")
                render96sel()
            time.sleep(2)
            buildspeed1 = input(f'''{Fore.BLUE}The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
        else:
            print(f"{Fore.RED}Invalid Option")
    elif confirmation == "n":
        reposelect()

def sm64exsel():
    print(f"\n{Fore.GREEN}You have selected SM64ex.")
    smexconf = input(f"\n{Fore.BLUE}Is the above selection correct (y,n) ")
    if smexconf == "y":
        branchsmex = input('''Which branch to clone and build? \n
        1. Nightly (Good enough for daily players)
        2. Master (Outdated, recommended to use any other branch..)
        3. Coop (Puts a spin on the game. In this fork, you can now play with friends.)
        4. Alo (Adds quality-of-life fixes to the game like adding Puppycam, revamping the Pause Menu and many other improvements.)
        5. There are more branches to come. Stay tuned for more of your favourite branches. ''')
        if branchsmex == "1":
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/sm64pc/sm64ex --branch nightly")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex/baserom.us.z64")
            print("Baserom copied.\n")
            time.sleep(2)
            buildspeed1 = input('''The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/sm64pc/sm64ex --branch master")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex/baserom.us.z64")
            print("Baserom copied.")
            time.sleep(2)
            buildspeed1 = input('''The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            print("\nConfirm you have copied baserom.us.z64 to your home folder.")
            time.sleep(3)
            os.system("git clone https://github.com/djoslin0/sm64ex-coop")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex-coop/baserom.us.z64")
            print("Baserom copied.\n")
            time.sleep(2)
            buildspeed1 = input('''The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/AloXado320/sm64ex-alo")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64ex-alo/baserom.us.z64")
            print("Baserom copied.\n")
            time.sleep(2)
            buildspeed1 = input('''The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            
        else:
            print(f"{Fore.RED}Invalid Option")
    elif smexconf == "n":
        reposelect()

def sm64rtsel():
    sm64rtconf = input("You have selected SM64RT. You will be asked to select which branch to clone after the confirmation. Input yes or no! (NOT y or n) ")
    if sm64rtconf == "yes":
        branchsm64rt = input('''You have selected SM64RT. Here are the two available branches:
        1. Master
        2. fsr''')
        if branchsm64rt == "1":
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/DarioSamo/sm64rt --branch master")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64rt/baserom.us.z64")
            print("Baserom copied.\n")
            time.sleep(2)
            buildspeed1 = input('''The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
            print("\nConfirm you have copied baserom.us.z64 to your home folder.\n")
            time.sleep(3)
            os.system("git clone https://github.com/DarioSamo/sm64rt --branch fsr")
            print("Copying baserom....")
            os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/sm64rt/baserom.us.z64")
            print("Baserom copied.\n")
            time.sleep(2)
            buildspeed1 = input('''The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
        else:
            print(f"{Fore.RED}Invalid Option")

def saturnsel():
    saturnconfirm = input("You have selected Saturn. \nIs the above selection correct? (y,n) ")
    if saturnconfirm == "y":
        print("\nPut your Super Mario 64 baserom in your home folder andrename it to baserom.us.z64\n")
        time.sleep(3)
        os.system("git clone https://github.com/Llennpie/Saturn --branch legacy")
        print("Copying baserom....")
        os.system("cp /home/$USER/baserom.us.z64 /home/$USER/TuxBuilder64/Saturn/baserom.us.z64")
        print("Baserom copied.")
        print("You will be asked to enter your Sudo password in a second. This is to fix an issue with building on Linux, where make spits out a 'No such file or disrectory' error about the file 'json/json.h'.")
        time.sleep(1)
        os.system("sudo ln -s /usr/include/jsoncpp/json/ /usr/include/json")
        time.sleep(2)
        buildspeed1 = input('''The repository has been cloned and the baserom has been successfully copied. Select the speed by which to build the game.
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
    elif saturnconfirm == "n":
        reposelect()
    else:
        print(f"{Fore.RED}Invalid Option")


if repo == "1":
    render96sel()
elif repo == "2":
    sm64exsel()
elif repo == "3":
    sm64rtsel()
elif repo == "4":
    saturnsel()
else:
    print("Invalid input. Try again. \n")
    reposelect()

print(f"{Fore.RED}If you encounter any problems in building, try again, and follow the instructions properly.")
