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
font("../../fonts/amiri/Amiri-Bold.ttf")
for frame in range(F):     
    new_page()
    font("../../fonts/amiri/Amiri-Bold.ttf")
    grid() # Toggle for grid view
    fill(0)
    rect(M*2, M*4,M*5,M*2)
    rect(M*9, M*4,M*5,M*2)
    fill(1)
    
    stroke(None)
    tracking(None)
    
    fontSize((M*1.3))
    tracking(-1.0)
    text("Hal min", (M*9.3, M*3.3))
   
    fontSize((M*2))
    tracking(None)
    text("هل من", (M*2.1, M*2.9))
    
    fontSize((M*1.3))
    tracking(-1.0)
    text("Hal min", (M*9.3, M*3.3))
     
    t = 0
    for i in range(12):
        stroke(2)
        fill(0)
        y = sin(a+t)*64
        oval((M*2)+(i*64), (M*2)+y, M, M)
        t += 0.1
    print(y)
    a += 0.1
saveImage("11.gif")