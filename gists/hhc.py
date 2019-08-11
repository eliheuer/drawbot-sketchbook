# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN
W,H,M = 1024,512,64

# EDGE
def edge():
    stroke(1)
    strokeWidth(1)
    fill(None)
    rect(M+M, M+M, W-(4*M), H-(4*M))

# GRID
def grid():
    stroke(1)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(13):
        polygon(((M+M)+stpX, M+M), ((M+M)+stpX, H-(M+M)))
        stpX += incX
    for y in range(5):
        polygon((M+M, (M+M)+stpY), (W-(M+M), (M+M)+stpY))
        stpY += incY

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)
    # font("fonts/BlobGX.ttf")
    #for axis, data in listFontVariations().items():
    #    print((axis, data))
    # fontVariations(wght=500)

# MAIN PAGE 
new_page()
grid() # Toggle for grid view
edge() # Toggle for safe area

fill(1)
#rect(M*5, M*0,M*18,M*1)
#rect(M*27,M*0,M*18,M*1)

font("../fonts/Pilowlava-Regular.otf")
fill(1)
stroke(None)
tracking(-8)
fontSize((M*1))
text("PILOWLAVA", (1.1*M, (M*5.3)))
#text("LINUX", (6.45*M,    (M*5.3)))
tracking(None)
font("../fonts/bluu/BluuNext-Bold.otf")
for axis, data in listFontVariations().items():
    print((axis, data))
fontSize((M*4))
#text("Eye Opener", (5*M, (M*13)))

step = 0
for i in range(17):
    stroke(0)
    fill(step)
    step += 0.07
    #oval(M*(27+i),M*13,M*2,M*2)

stepb = 0.-1
y = 0
for i in range(145):
    stroke(1)
    fill(stepb)
    stepb += 0.004
    temp = sin(i/4)*110
    y = temp
    oval(M+(i*6),y+(M*2),M,M)
#oval(M*2,M*22,M*2,M*2)

saveImage("image.png")