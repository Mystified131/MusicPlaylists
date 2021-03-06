#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from pathlib import Path
import shutil
from RandFunct import random_number
from RandFunct2 import random_number2

def permutList(l):
    if not l:
            return [[]]
    res = []
    for e in l:
            temp = l[:]
            temp.remove(e)
            res.extend([[e] + r for r in permutList(temp)])

    return res


def remaplist(lst):
    rnalst = []
    l4 = lst.pop()
    l3 = lst.pop()
    l2 = lst.pop()
    l1 = lst.pop()
    rnalst.append(l1)
    lst.append(l1)
    rnalst.append(l2)
    lst.append(l2)
    rnalst.append(l3)
    lst.append(l3)
    rnalst.append(l4)
    lst.append(l4)
    rnatot = permutList(rnalst)
    x = len(lst)
    y = (x // 4) + 1
    outlst = []
    for z in range(y):
        ctr = random_number(24)
        addlst = rnatot[ctr]
        outlst.append(addlst)
    finlst = []
    for elem in outlst:
        for elem2 in elem:
            if len(finlst) <= x:
                finlst.append(elem2)
    fonlst = []
    for a in range(x):
        val = (lst[a] + finlst[a])
        if val >= (max(lst)-1):
            val -= max(lst)
        if val in fonlst:
            val += 1
        fonlst.append(val)
    return fonlst

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))

print("")

totrk = int(input("How many tracks would you like to add to this playlist? The minimum is 5 and the default is 50: "))

if not totrk:
    totrk = 50 #This variable controls length of output playlist

if totrk <= 4:
    totrk = 5

print("")

cpy = str(input ("Would you like to copy these files to the static folder? To copy is the default. If so, please press 'Y': "))

if not cpy:
    cpy = "Y" #This variable controls whether we copy the files to the static folder

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

srchstr = 'E:\\OriginalAudio\\Songs'

#srchstr = 'C:\\Users\\mysti\\Downloads'

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

print("")

print("Please wait while the processor applies organic logic to your track collection.")

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

leng = len(newply)

newlst = []

startlen = random_number(leng -totrk)

for x in range(startlen, (startlen + totrk)):
    newlst.append(x)

fonlst = remaplist(newlst)

finlst = [] 

outlst = []

for y in range(totrk
):
    valu = fonlst[y]
    if valu > leng:
        valu -= random_number(leng)
    finlst.append(newply[valu])
    trk =  str(Path(newply[valu]).stem)
    p = (Path(newply[valu]))
    trkloc = str(p.parts[-2])
    sttrk = str(y + 1) + " " + trkloc + ": " + trk
    if cpy == "Y":
        outstr = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\static\\" + str(tim) + "_" + str((y + 1)/100) + trkloc + "-__" + trk + ".wav"
        shutil.copy(newply[valu], outstr)
        print("")
        print("Copying: " + str(y+1))
    outlst.append(sttrk)
    newply.remove(newply[valu]) 

srchstr2 = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\static\\"

contentloc = []

for subdir, dirs, files in os.walk(srchstr2):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") :

            cstr = str(filepath)
            contentloc.append(cstr)

ounam = "CloneOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close() 

ounm = "CloneOrderedTracklist_" + time + ".txt"

outfile = open(ounm, "w")

for elem in outlst:
     outfile.write(elem + '\n')

outfile.close() 

ounm2 = "CloneOrderedLocalPlaylist_" + time + ".m3u"

outfile = open(ounm2, "w")

for elem in contentloc:
     outfile.write(elem + '\n')

outfile.close() 

print("")

print("The documents are located in the same folder as this code. If tracks were copied, they will be in the static folder.")

print("")

## THE GHOST OF THE SHADOW ##
