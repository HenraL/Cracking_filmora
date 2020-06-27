from time import sleep
import platform
import os
import shutil
#color 0A
#echo off
def start(a):
    try:
        os.system("{}".format(a))
    except:
        print("Nothing has happened because you're either not on a pc or your comand prompt is damaged and so is missing some command lines.")
def copy(src, dest):
    shutil.copy(src, dest)
def pause():
    pause=input("Press enter to continue...")
def cd(r):
    os.system("cd {}".format(r))
def copy(file, target):
    try:
        os.system()
    except:
        print("Wondershare Filmora is not in programfiles(x86)")
    try:
        os.system()
    except:
        print("Wondershare Filmora is not in programfiles")
    print()
    print("Make shure you have installed Wondershare Filmora 9.X.X in one of the common places (program file(x86) or programfiles).")
    print("If this is not the case, but you have installed Wondershare Filmora, please enter the path to access it")
    print("A path is composed of:")
    print("- The letter of the disk that is concerned (C, D, E, etc)")
    print("- The folders to acces the required target (The letter\my first folder\my second Folder\The target)")
    print()
    disk=input("Please enter the letter of the disk containing the filmora software (C, D, E, etc):")
    souce="{}:/".format(disk)
    folders=int(input("Please enter the number of folder or subfolders that separate the program (the folder containing the program is excluded (the name of that folder is Wondershare)) from the source of the disk. (The letter is called the source):"))
    for i in folders:
         follder=input("Please enterthe name of the folder n°{}:".format(i))
        path+="{}/".format(follder)
    path+="Wondershare/Filmora{}".format(fversion)
    testpcont="cont"
    while testpcont=="cont":
        print("The path is '{}'".format(path))
        print("You can check to see if the path is wright by copy/pasting the following path: {}".format(path))
        testp=input("Enter T or t for the program to test the path, otherwise leave this question empty")
        if testp=="t" or testp=="T":
            try:
                start(path)
            except:
                print("Nothing has happened because you're either not on a pc or your comand prompt is damaged and so is missing some command lines.")
        elif testp=="" or testp==" " or testp=="    ":
            copy("files/PYG64(1).dll","{}{}PYG64.dll".format(source,path))
            copy("files/winmm(1).dll","{}{}winmm.dll".format(source,path))
        else:
        
    
def cls():
    if platform.system=="Windows":
        os.system("cls")
    elif platform.system=="Linux":
        os.system("clean")
    else:
        print("please run this program under windows")
cls()
print("Before we start")
fversion=int(input("Please enter the first number of the version of filmora that you're trying to crack (example: in 9.X.X you will enter 9):"))
contiinue="go"
while contiinue=="go":
    print("If you encounter problems like acces denied, try running the program with admin wrights.")
    print("If problems persist visit the debug section.")
    choice=input("Do you wish to legaly crack filmora 9? [(y)es/(n)o/(d)ebug/(e)xit]:")
    if choice=="y" or choice=="Y":
        print("Extracting files.....")
        sleep(2)
        print("Copying files........")
        cd files
        echo on
        REM Below if the first line to modify if needed
        copy PYG64.dll "c:\Program Files\Wondershare\Filmora9"
        REM Below is the second line to modify if needed
        copy winmm.dll "c:\Program Files\Wondershare\Filmora9"
        echo off
        print("Files extracted")
        pause()
        goto goodbye
elif choice=="n" or choice=="N":
    echo Extraction aborded: You have refused to extract the files.
pause()
goto goodbye
elif choice=="d" or choice=="D":
    print("=============================================== The Debug Guide =======================================================")
    print("################################################ Important note #######################################################")
    print("#                         Please note that the following actions require to edit this program                         #")
    print("#                         Therefore I Recomend that you take a screenshot of the following points                     #")
    print("#                                                                                                                     #")
    print("#                                              To edit the code                                                       #")
    print("#                                      Right click on the file --> edit                                               #")
    print("#                                A file will open with displaying the program                                         #")
    print("#                  From there you will just need to follow the guided steps and save you're changes                   #")
    print("#                                                                                                                     #")
    print("#                       Don't forget to run the program once you've saved you're modifications                        #")
    print("#                                                                                                                     #")
    print("#                                 If you have not done this kind of manipulation before                               #")
    print("#                                                      or                                                             #")
    print("#                                      Aren't shure of what you are doing                                             #")
    print("#                                                                                                                     #")
    print("#                        I strongly advise you make a copy of the file before you start editing.                      #")
    print("#                                                                                                                     #")
    print("#                                To help you, I have put coments on the lines to edit                                 #")
    print("#######################################################################################################################")
    print(".____________________________________________________________________________________________________________________.")
    print("|                                      You can find these files at:                                                  |")
    print("|                                      The bat file:                                                                 |")
    print("|                                      https://bit.ly/3dnBjqY                                                        |")
    print("|====================================================================================================================|")
    print("|                                      The python version (better develloped, better guided):                        |")
    print("|                                      https://bit.ly/2No5Bzh                                                        |")
    print("|____________________________________________________________________________________________________________________|")
    print("If the copy failes please check the following ellemnts:")
    print("1. Check that you have all the required files")
    print("1.1 This means you have")
    print("1.1.1 This file")
    print("1.1.2 A folder named files")
    print("1.1.3 In this folder a file named PYG64.dll (depending on your settings you will or not see the extension .dll)")
    print("1.1.4 In this same folder a file named winmm.dll (depending on your settings you will or not see the extension .dll)")
    print()
    print("If these previous steps are validated checke the second steps.")
    print()
    print("""2. Check that you're current disk is labeled (C:) If this is no the case replace the letter c (in the line "c:\Program Files\Wondershare\Filmora9" by the lowercase letter of your disk in which the program is)""")
    print("""2.1 Check that the folder "Wondershare" is located in The folder "Program Files" if this is not the case please change "Program Files" by the folder the folder in which the program is.""")
    print()
    print("PS: To find the folder, wrigt click on the icon on your desktop --> reveal in explorer, repeat this action with the icon in the folder in which you'lle be if you do not see more than the shortcuts to Uninstall Wondershare Filmora9 and Wondershare Filmora9.")
    print()
    print("If all these requirements are fufiled you should not encounter anymore problems in this software.")
    print()
    pause()
    pause()
    continue
else:
    print("Please enter y or Y for yes or n or N for no or d or D for manual debug.")
    print("You have entered {}.".format(choice))
    continue


:n

:d

goto goodbye
:goodbye
echo Goobye, See you next time
echo File Created By Henry Letellier
echo PS:
echo Please forgive me for my spelling mistakes.
echo This is a freeware program, use at you're own risk.
pause()
pause()
