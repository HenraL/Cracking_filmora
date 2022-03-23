color 0A
echo off
cls
:start
echo This Program will work for versions 9 and below
echo If you encounter problems like acces denied, try running the program with admin wrights.
echo If problems persist visit the debug section.
echo Enter the version of your copy of filmora (9, 8, etc... not 9.2 or 8.4):
set /p versionOfProg=
echo Do you wish to legaly crack filmora %versionOfProg%? [(y)es/(n)o/(d)ebug]:
set /p choice=
if %choice%==y goto y
if %choice%==Y goto y
if %choice%==n goto n
if %choice%==N goto n
if %choice%==d goto d
if %choice%==D goto d
echo Please enter y or Y for yes or n or N for no or d or D for manual debug.
echo You have entered %choice%
goto start
:y
echo Extracting files.....
cd files
echo first atempt.
echo on
REM Below is the first line to modify if needed
copy PYG64.dll "c:\Program Files\Wondershare\Filmora%versionOfProg%"
REM Below is the second line to modify if needed
copy winmm.dll "c:\Program Files\Wondershare\Filmora%versionOfProg%"
REM second atempt.
REM Below is the first line to modify if needed
copy PYG64.dll "c:\Program Files\Wondershare\Wondershare Filmora"
REM Below is the second line to modify if needed
copy winmm.dll "c:\Program Files\Wondershare\Wondershare Filmora"

echo off
echo Files extracted
pause
goto goodbye
:n
echo Extraction aborded: You have refused to extract the files.
pause
goto goodbye
:d
echo =============================================== The Debug Guide =======================================================
echo ################################################ Important note #######################################################
echo #                         Please note that the following actions require to edit this program                         #
echo #                         Therefore I Recomend that you take a screenshot of the following points                     #
echo #                                                                                                                     #
echo #                                              To edit the code                                                       #
echo #                                      Right click on the file --> edit                                               #
echo #                                A file will open with displaying the program                                         #
echo #                  From there you will just need to follow the guided steps and save you're changes                   #
echo #                                                                                                                     #
echo #                       Don't forget to run the program once you've saved you're modifications                        #
echo #                                                                                                                     #
echo #                                 If you have not done this kind of manipulation before                               #
echo #                                                      or                                                             #
echo #                                      Aren't shure of what you are doing                                             #
echo #                                                                                                                     #
echo #                        I strongly advise you make a copy of the file before you start editing.                      #
echo #                                                                                                                     #
echo #                                To help you, I have put coments on the lines to edit                                 #
echo #######################################################################################################################
echo ".____________________________________________________________________________________________________________________."
echo "|                                      You can find these files at:                                                  |"
echo "|                                      The bat file:                                                                 |"
echo "|                                      https://bit.ly/3dnBjqY                                                        |"
echo "|====================================================================================================================|"
echo "|                                      The python version (better develloped, better guided):                        |"
echo "|                                      https://bit.ly/2No5Bzh                                                        |"
echo "|____________________________________________________________________________________________________________________|"
echo If the copy failes please check the following elements:
echo 1. Check that you have all the required files
echo 1.1 This means you have
echo 1.1.1 This file
echo 1.1.2 A folder named files
echo 1.1.3 In this folder a file named PYG64.dll (depending on your settings you will or not see the extension .dll)
echo 1.1.4 In this same folder a file named winmm.dll (depending on your settings you will or not see the extension .dll)
echo.
echo If these previous steps are validated check the second steps.
echo.
echo 2. Check that you're current disk is labeled (C:) If this is no the case replace the letter c (in the line "c:\Program Files\Wondershare\Filmora%versionOfProg%" by the lowercase letter of your disk in which the program is)
echo 2.1 Check that the folder "Wondershare" is located in The folder "Program Files" if this is not the case please change "Program Files" by the folder the folder in which the program is.
echo.
echo PS: To find the folder, wrigt click on the icon on your desktop --> reveal in explorer, repeat this action with the icon in the folder in which you'll be if you do not see more than the shortcuts to Uninstall Wondershare Filmora%versionOfProg% and Wondershare Filmora%versionOfProg%.
echo.
echo If all these requirements are fufiled you should not encounter anymore problems in this software.
echo.
pause
pause
goto start
goto goodbye
:goodbye
echo Goobye, See you next time
echo File Created By Henry Letellier
echo PS:
echo Please forgive me for my spelling mistakes.
echo This is a freeware program, use at you're own risk.
pause
pause