import random
import os
from collections import defaultdict
import datetime
from pathlib import Path
import shutil

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
   
srchstr = 'E:\\OriginalAudio\\Songs'

print("")

print("Please wait while the processor applies organic logic to your track collection.")

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") or filepath.endswith(".mp3") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

mapl = []

mapld = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    mapl.append(w)
    mapld.append(contentdat[w])

#hopl = [(0, -2), (0, -1), (0, 0), (0 , 1,), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2)]

hopl = []

for obj in range(random.randrange(18,36)):
    a = random.randrange(-2, 2)
    b = random.randrange(-2, 2)
    hopl.append((a,b))

moves = 50

fst = random.randrange(len(mapl))

outlst = []

finlst = [] 

for ctr in range(totrk):
    hopran = random.randrange(len(hopl))
    aval = (sum(int(i) for i in hopl[hopran])) * 4
    fst += aval
    astr = mapl[fst]

    trk =  str(Path(astr).stem)
    p = (Path(astr))
    trkloc = str(p.parts[-2])
    sttrk = str(ctr + 1) + " " + trkloc + ": " + trk
    if cpy == "Y":
        outstr = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\static\\" + str(tim) + "_" + str((ctr + 1)/100) + "_" + trkloc + "-__" + trk + ".wav"
        shutil.copy(astr, outstr)
        print("")
        print("Copying: " + str(ctr+1))
    outlst.append(sttrk)
    finlst.append(astr)
    mapl.remove(astr)

    bighop = random.randrange(10)
    if bighop > 7:
        fst = random.randrange(len(mapl))

srchstr2 = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\static\\"

contentloc = []

for subdir, dirs, files in os.walk(srchstr2):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") :

            cstr = str(filepath)
            contentloc.append(cstr)

ounam = "ToadOrderedPlaylist_" + time + ".m3u"

outfile = open(ounam, "w")

for elem in finlst:
     outfile.write(elem + '\n')

outfile.close() 

ounm = "ToadOrderedTracklist_" + time + ".txt"

outfile = open(ounm, "w")

for elem in outlst:
     outfile.write(elem + '\n')

outfile.close() 

ounm2 = "ToadOrderedLocalPlaylist_" + time + ".m3u"

outfile = open(ounm2, "w")

for elem in contentloc:
     outfile.write(elem + '\n')

outfile.close() 

print("")

print("The documents are located in the same folder as this code. If tracks were copied, they will be in the static folder.")

## THE GHOST OF THE SHADOW ##



