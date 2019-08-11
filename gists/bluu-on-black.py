# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/
# 🌍 GIT URL: https://github.com/eliheuer/drawbot-sketchbok

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN
W,H,M = 1000,500,20

# EDGE
def edge():
    stroke(0.1)
    strokeWidth(1)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID
def grid():
    stroke(0.1)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(48):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(32):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)
    # LOAD BASIC FONT
    # font("fonts/BlobGX.ttf")
    # Set axis from font
    #for axis, data in listFontVariations().items():
    #    print((axis, data))
    # Set variation 
    # fontVariations(wght=500)

# MAIN PAGE 
new_page()
#grid() # Toggle for grid view
#edge() # Toggle for safe area

fill(1)
#rect(M*5, M*0,M*18,M*1)
#rect(M*27,M*0,M*18,M*1)

font("../fonts/Pilowlava-Regular.otf")
fill(1)
stroke(None)
tracking(-1.5)
fontSize((M*2.5))
text("A NEW RULE", (5*M, (M*22)))

tracking(None)
font("../../../Type/forks/Sofia-Sans/sources/variable_ttf/NewFont-VF.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))
fontSize((M*1))
lineHeight(M*1.4)

textBox(
    "It is the rule with drunkards to fall upon each other, to quarrel, become violent, and make a scene. The lover is even worse than a drunkard. I will tell you what love is: to enter a mine of gold. And what is that gold?",
(M*5, M*6, M*20, M*15), align="left")

textBox(
    "The lover is a king above all kings, unafraid of death, not at all interested in a golden crown. The dervish has a pearl concealed under his patched cloak. Why should he go begging door to door?",
(M*5, M*3, M*20, M*10), align="left")
""

textBox(
    "Last night that moon came along, drunk, dropping clothes in the street. “Get up,”",
(M*5, M*-10.2, M*22, M*15), align="left")

textBox(
    "I told my heart, “Give the soul a glass of wine. The moment has come to join the nightingale in the garden, to taste sugar with the soul-parrot.”",
(M*27, M*6, M*20, M*15), align="left")

textBox(
    "I have fallen, with my heart shattered—where else but on your path? And I broke your bowl, drunk, my idol, so drunk, don't let me be harmed, take my hand.",
(M*27, M*-0.6, M*20, M*15), align="left")

textBox(
    "A new rule, a new law has been born: break all the glasses and draw near to the glassblower.",
(M*27, M*-7.4, M*18, M*15), align="left")

textBox(
    "—Rumi",
(M*27, M*-1, M*20, M*3), align="left")

step = 0
for i in range(12):
    stroke(0)
    fill(1, step, 0)
    step += 0.1
    oval(M*(27+i),M*22,M*2,M*2)
#oval(M*2,M*22,M*2,M*2)

#saveImage("image.png")