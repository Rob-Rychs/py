
import time
local =time.asctime( time.localtime(time.time()) )
with open("JT Tools Log File.txt", "a") as f: f.write(local)
print ("Sleeping...")

with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools Initialized:version 6.2.0\n")
print ("This script is copyrighted by Jensen Taylor 2014 - 2016(C). JT Tools script version 6.2.0 Beta Re-Written for Python 2.7 instead of 3.4 due to a bug in python 3.4.1.")
print ("Importing module os....")

import os,subprocess
print ("Module os has been imported successfully.")
print ("Importing module time...")

print ("Importing module sys...")


os.system ("color f9")
time.sleep (2)
repeat = int(input("Please enter 1 to confirm you are not a robot."))
while repeat == int(1):
 code = int(518082)
 codeenter = int(input("Please enter the current NPIN."))
 while codeenter != code:
     print("Sorry you got the code wrong.")
     codeenter = int(input("Please enter the current NPIN."))
     local =time.asctime( time.localtime(time.time()) )
     with open("JT Tools Log File.txt", "a") as f: f.write(local)
     with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Incorrect PIN entered.\n")
 if code == int(518082):
  local =time.asctime( time.localtime(time.time()) )
  with open("JT Tools Log File.txt", "a") as f: f.write(local)
  with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Correct PIN entered.\n")
 
    
 print ("Here is a list of modes available:")
 print ("1= Restart")
 print ("2 = Logoff")
 print ("3 = Alternative Logoff Method ")
 print ("4 = Hibernate")
 print ("5= Shutdown")
 print ("6 = Alternative Shutdown Method")
 print ("7 = Colour Flickr")
 print ("8 = Call CMD")
 print ("9 = Call Documents")
 print ("10 = Call A Python Shell")
 print ("11 = Call Task Manager")
 print ("12 = Create folders in the same directory as this script.")
 print ("13 = Remove Directories")
 print ("14 = Create Files")
 print ("15 = Restart This Script (debug purposes)")
 print ("16 = Perform Operations With Numbers")
 print ("17 = Lock This Script")
 print ("18 = Call Auto-Clicker")
 print ("19 = Exit")
 modewanted = int(input("Please enter the number of the mode that you want."))
 if modewanted == 1:
  shutdown = int(input("Please enter 1 or 0 to confirm restart."))
  local =time.asctime( time.localtime(time.time()) )
  with open("JT Tools Log File 6.2.0.txt", "a") as f: f.write(local)
  with open ("JT Tools Log File 6.2.0.txt","a") as f: f.write("    JT Tools :Restart (mode 1) entered.\n")
  
  if shutdown == 1:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -r -f")
     os.system ("shutdown -l -f")
 if modewanted == 2:
  logoff = int(input("Please enter 1 or 0 to confirm logoff."))
  if logoff == 1:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -l -f")
 if modewanted == 4:
  hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
  if hibernate == 1:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -h -f")
 if modewanted == 5:
  shutdown = int(input("Please enter 1 or 0 (no) to confirm shutdown."))
  if shutdown == 1:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -s -f")
 if modewanted == 7:
  suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
  if suretoflash == 1:
    howlongtoflashfor = int(input("How many flashes do you wish to occur?"))
    currentflashes= int(0)                       
    while howlongtoflashfor != currentflashes:
     os.system ("color 4a")
     os.system ("color f9")
     currentflashes = currentflashes+1
 if modewanted == 8:
    subprocess.call("cmd.exe")
 if modewanted == 19:
  print ("Closing!!!")
  closing = 5
  while closing !=6 and closing >0.015:
    closing = closing -0.017
    print ("Closing in",(round(closing, +3)),"seconds.")
    time.sleep (0.017)
  if closing == 0.002 or closing<0.002:
    exit(None)
 if modewanted == 9:
    subprocess.call("explorer.exe")
 if modewanted == 10:
   subprocess.call("python.exe")
 if modewanted ==3:
  altlogoff = int(input("Please enter 1 or 0 to confirm logoff."))
  if altlogoff ==1:
    waittime =int(input("How long, in minutes, do you wish to wait before logoff proceeds?"))
    time.sleep(waittime*60)
    subprocess.call ("logoff.exe")
 if modewanted == 6:
  altshutdown =int(input("Please enter 1 or 0 to confirm shutdown."))
  if altshutdown ==1:
    waittime = int(input("How long, in minutes, do you wish to wait before shutdown proceeds?"))
    time.sleep (waittime*60)
    subprocess.call ("shutdown.exe")
 if modewanted == 12:
   foldername = raw_input("Please input the name of your new folder.")
   os.makedirs (foldername)
   cont = raw_input("Success! Press any key then enter to continue...")
 if modewanted == 15:
  confirmscriptrestart= int(input("Please input 1 to confirm restarting of this script."))
  if confirmscriptrestart == 1:
    subprocess.call ( "JT Tools 6.2.0.py", shell =True)
 if modewanted == 16:
  print ("Here is a list of operations:")
  print ("1 =Add")
  print ("2 = Take")
  submode = int(input("Please enter the number of the operatino you wish to perform>"))
  if submode == 1 or 2:
    check = int(0)
    startnum = int(input("Please enter your starting number."))
    addortakenum = int(input("Please input the number to be added. If you wish to take a number please put a - and then the number you wish to be taken."))
    endnum=int(input("Please enter your end number."))
    waittime = int(input("How long do you wish to wait before each operation is performed?"))
    if endnum>startnum:
     while endnum>startnum:
        print(startnum)
        if addortakenum<int(0):
            startnum = startnum-addortakenum
        if addortakenum>int(0):
            startnum = startnum+addortakenum
        time.sleep(waittime)
     if startnum ==endnum or startnum>endnum:
        print("The closest number to your target number was:",startnum)
        time.sleep (1)
    if startnum>endnum and check !=int(1):
     while startnum>endnum:
        print (startnum)
        if addortakenum<0:
            startnum = startnum+addortakenum
        if addortakenum>0:
            startnum = startnum = startnum-addortakenum
        time.sleep (waittime)
     if startnum == endnum or startnum<endnum:
        print ("The closest number to your target end number was:",startnum)
        time.sleep (1)
 if modewanted == 13:
   foldername = raw_input("Please input the name of the folder you wish to delete.")
   os.rmdir (foldername)
   cont = raw_input("Success! Press any key then enter to continue...")
 if modewanted == 14:
    import io,time
    filename = raw_input("Please enter your file name plus the extension, eg. B.txt.  ")
    with io.FileIO(filename, "w"):
      time.sleep (1)
 if modewanted == 11:
   subprocess.call("taskmgr.exe")
 if modewanted == 17:
     print ("Locked!!!")
 if modewanted == 18:
  subprocess.call("\\Autoclicker.exe")
if repeat != 1:
    exit(None)
    



 
  


        
                     




      
           
            
