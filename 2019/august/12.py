# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com

from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,512,64,64

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

# MAIN
a = 0
for frame in range(F):     
    new_page()
    font("../../fonts/Pilowlava-Regular.otf")
    grid() # Toggle for grid view
    fill(0)
    rect(M*2, M*5,M*5,M*1)
    fill(1)
     
    t = 0
    f = 0
    for i in range(12):
        stroke(2)
        y = sin(a+t)*96
        f = y*0.01
        fill(1,f,f/2)
        stroke(1,f,f/2)
        oval((M*2)+(i*64), (M*3.5)+y, M, M)
        t += 0.1
    print(y)
    
    stroke(1)
    strokeWidth(2)
    fill(0)
    tracking(None)
    fontSize((M*1))
    text("FOOBAR", (M*2, M*5.1))
    
    a += 0.1
saveImage("12.gif")