#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from pathlib import Path

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
    mxval = max(lst)
    sbval = int(mxval / 4)
    outlst = []
    for elem in lst:
        divedic = random.randrange(10)
        if divedic < 8:
            adr = random.randrange(sbval)
            elem += adr
            if elem > mxval:
                elem -= mxval
            outlst.append(elem)
        if divedic > 7:
            val = random.randrange(mxval)
            outlst.append(val)
    return outlst


#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))
   
totrk = 50 #This variable controls length of output playlist

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


leng = len(newply)

newlst = []

startlen = random.randrange(leng -totrk)

for x in range(startlen, (startlen + totrk)):
    newlst.append(x)

fonlst = remaplist(newlst)

finlst = [] 

outlst = []

for y in range(totrk):

    valu = fonlst[y]
    if valu > leng:
        valu -= random.randrange(leng)
    finlst.append(newply[valu])
    trk =  str(Path(newply[valu]).stem)
    p = (Path(newply[valu]))
    trkloc = str(p.parts[-2])
    sttrk = trkloc + ": " + trk
    outlst.append(sttrk)
    newply.remove(newply[valu])

ounam = "DreamFrogOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close() 

ounm = "DreamFrogOrderedTracklist_" + time + ".txt"

outfile = open(ounm, "w")

for elem in outlst:
     outfile.write(elem + '\n')

outfile.close() 

## THE GHOST OF THE SHADOW ##
