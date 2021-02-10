#This code imports the necessary modules.

import os
import datetime
from pydub import AudioSegment

#def joinsound(content):
    #if len(content) == 1:
        #ctrack = content[0]
        #newAudio = AudioSegment.from_wav(ctrack)

    #else:
       # ctrack = content[0]
        #newAudio = AudioSegment.from_wav(ctrack) + Audiosegment.from.wav(joinsound(content[1:]))
        #content.pop()



right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

srchstr = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\"

content = []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") :

            cline = str(file)
            content.append(cline)

print(content)

atrack = content[0]

newAudio = AudioSegment.from_wav(atrack)

for ctr in range(1, len(content)):

    try: 
        atrack = content[ctr]

        tempAudio = AudioSegment.from_wav(atrack)
        newAudio += tempAudio

    except:
        print("")
        print("Memory Limit Reached.")
  

oufil = "C:\\Users\\mysti\\Coding\\MusicPlaylists\\static\\" + tim + "_Audiomix.wav"

try: newAudio.export(oufil, format="wav")

except:
    print("")
    print("Output error.")

print("")

print("Finished file located in static folder.")

## THE GHOST OF THE SHADOW ##
