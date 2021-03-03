from subprocess import call

print("")

ch = str(input("Would you like a playlist by 'A'ant, 'C'lone, 'D'ream Frog, 'T'oad, or 'R'NA?: "))

if not ch or (ch not in ['A', 'C', 'D', 'T', 'R']):
    ch = 'R'

if ch == 'A':
    call(["python", "PlaylistByAnt.py"])

if ch == 'C':
    call(["python", "PlaylistByClone.py"])

if ch == 'D':
    call(["python", "PlaylistByDreamFrog.py"])

if ch == 'T':
    call(["python", "PlaylistByToad.py"])

if ch == 'R':
    call(["python", "PlaylistByRNA.py"])

## THE GHOST OF THE SHADOW ##