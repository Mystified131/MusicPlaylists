#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from pathlib import Path
import shutil

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
    l4 = max(lst)
    l1 = int(l4 / 4)
    l2 = int(l4 / 2)
    l3 =  l1 + l2
    rnalst.append(l1)
    rnalst.append(l2)
    rnalst.append(l3)
    rnalst.append(l4)
    rnatot = (permutList(rnalst))
    x = len(lst)
    y = (x // 4) + 1
    outlst = []
    for z in range(y):
        ctr = random.randrange(24)
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

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") or filepath.endswith(".mp3") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

newlst = []

startlen = random.randrange(totlen -100)

for x in range(startlen, startlen + 100, 2):
    newlst.append(x)

fonlst = remaplist(newlst)

finlst = [] 

outlst = []

for y in range(totrk):
    valu = fonlst[y]
    if valu > totlen:
        valu -= totlen

    finlst.append(newply[valu])
    trk =  str(Path(newply[valu]).stem)
    p = (Path(newply[valu]))
    trkloc = str(p.parts[-2])
    sttrk = trkloc + ": " + trk
    if cpy == "Y":
        outstr = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\static\\" + str(tim) + "_" + trkloc + "-__" + trk + ".wav"
        shutil.copy(newply[valu], outstr)
    outlst.append(sttrk)
    newply.remove(newply[valu])

ounam = "RNAOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close()

ounm = "RNAOrderedTracklist_" + time + ".txt"

outfile = open(ounm, "w")

for elem in outlst:
     outfile.write(elem + '\n')

outfile.close() 

print("")

print("The documents are located in the same folder as this code. If tracks were copied, they will be in the static folder.")

## THE GHOST OF THE SHADOW ##
