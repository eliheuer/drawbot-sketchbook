# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,512,64,128

# GRID
def grid():
    stroke(2)
    strokeWidth(1)
    rect(M+M, M+M, W-(4*M), H-(4*M))
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(13):
        polygon(((M+M)+stpX, M+M),
                ((M+M)+stpX, H-(M+M)))
        stpX += incX
    for y in range(5):
        polygon((M+M, (M+M)+stpY),
                (W-(M+M), (M+M)+stpY))
        stpY += incY
        
# NEW PAGE
def new_page():
    newPage(W, H)
    frameDuration(1/24)
    fill(0)
    rect(-2, -2, W+2, H+2)
    # font("fonts/BlobGX.ttf")
    #for axis, data in listFontVariations().items():
    #    print((axis, data))
    # fontVariations(wght=500)

# MAIN
s = 0
font("../../fonts/Pilowlava-Regular.otf")
for frame in range(F): 
    new_page()
    font("../../fonts/Pilowlava-Regular.otf")
    grid() # Toggle for grid view
    fill(0)
    rect(M*2, M*5,M*5,M*1)
    
    fill(1)
    stroke(None)
    tracking(None)
    fontSize((M*1))
    text("FOOBAR   ", (M*2.05, M*5.15))
    
    step = 0
    for i in range(17):
        stroke(0)
        fill(step)
        step += 0.07
        #oval(M*(27+i),M*13,M*2,M*2)

    stepb = 0.-1
    y = 0
    for i in range(129):
        stroke(2)
        fill(stepb)
        stepb += 0.002
        temp = sin(i*s)*140
        y = temp
        oval(y+(M*2)+(i*5),
             y+(M*2),
             M,M)
    if frame == 60:    
        saveImage("10.png")
    s += 0.001
saveImage("10.gif")