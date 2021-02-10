#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime

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
    outlst = []
    for elem in lst: 
        adr = random.randrange(mxval)
        elem += adr
        if elem in outlst:
            elem += 1
        if elem <= mxval:
            outlst.append(elem)
        if elem > mxval:
            elem -= mxval
            outlst.append(elem)     
  
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

for y in range(totrk
):
    valu = fonlst[y]
    if valu > leng:
        valu -= random.randrange(leng)
    finlst.append(newply[valu])
  

ounam = "AntOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close() 

## THE GHOST OF THE SHADOW ##
