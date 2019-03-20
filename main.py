# Imports
from PIL import ImageGrab
import numpy as np
import time
from clicks import click


# Variables u need to set own your own according to your resolution. It is better if u change ur resolution to 1366x768
gamecords = [470, 410, 890, 411]
sgbox = [470, 470, 890, 471]
score = 0
d = [1250, 10]
f = [680, 630]


# For starting the game
click(d[0],d[1])
time.sleep(0.5)
click(f[0],f[1])
time.sleep(0.5)
fiimg = np.array(ImageGrab.grab(bbox=sgbox))
for x in range (0, sgbox[2]-sgbox[0], 120):
    if sum(fiimg[0][x]) // 3 <= 150:
        click(x + sgbox[0], sgbox[1]+3)
time.sleep(0.05)

# Function to update the value of x accordingly.
def checky(starttime,y,score):
    tscore = time.time() - starttime
    tcore = int(tscore)
    if (tcore >= 100) & (score <= 2500):
        return y + 75
    elif 4000 >= score > 2800:
        return y + 115
    elif score > 4000:
        return y + 140
    else:
        return y + 40

# Main part of coding which reads the screen and click on tiles.
st = time.time()
while True:
    img = np.array(ImageGrab.grab(bbox=gamecords))
    for x in range (0, gamecords[2]-gamecords[0], 120):
        if sum(img[0][x])//3 <= 80:
            actualy = checky(st, gamecords[3], score)
            if click( x + gamecords[0] + 10, actualy ) == True:
                score = score + 1
                print(score)