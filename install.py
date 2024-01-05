# made by xilliam
# use it as you want just credit me pleas
# this is shitty code after all

import easygui
import os
import subprocess
import shutil

# Used for getting the location of the lego city script folder
filename = None
# Thats where the default scripts end. Used to find a free point to install plugin
lvl=30

# really simple gui to make sure you want to install the plugin
if (easygui.ynbox('Start install?', 'Pizza Boy Mod Installer', ('Yes', 'No'))==True):
    pass
else:
    quit()

# opens a file explorer for you to select the script folder 
while(filename==None):
    filename=easygui.diropenbox("Please select the LEVELS\LEGO_CITY\LEGO_CITY\AI location")

print("Install location: "+filename) # mainly for debug

os.mkdir(filename+"/inst_tmp") #make tmp dir
# copy to temp loc
shutil.copyfile('./script.sf', filename+'/inst_tmp/script.sf')

# change to the dir we selected at the file explorer thingy
os.chdir(filename)

# finding a free "slot" for the plugin
file=open("SCRIPT.TXT", 'r')
content = file.read()
found=False # controls our while loop (on/off)
while (found==False):
    #print(lvl)
    if ("level"+str(lvl)) in content: # find the current level we are testing (example: if lvl=30 we are trying to find if level31 is already written in the file)
        print('level'+str(lvl)+" already exits! testing next one")
        # ugly code to make the computer COUNT THE NUMBERS!!
        tmp=int(lvl)+1 # convert lvl to int to add 1
        lvl=str(tmp) # making it a str again so we can use it (i love reading files)
        #print(lvl) # debug
    else:
        print('finally! level'+str(lvl)+" does not exist. embedding plugin there")
        file.close # for good measure
        found=True # cancel the loop

#print(lvl) #debug

# Importing the script to the file so that it loads
file=open("SCRIPT.TXT", 'a') 
file.write("\nlevel"+lvl) # making it load :)
file.close


# that was almost too easy
# now we need to copy the sf script :(

# copy from temp loc to real loc with correct name
shutil.copyfile('inst_tmp/script.sf', './level'+lvl+'.sf')
shutil.rmtree("inst_tmp")

print("install complete :)")
quit()