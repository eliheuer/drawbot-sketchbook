# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,512,64,126
frameDuration(1/30)

# GRID
def grid():
    stroke(0,0.5,1)
    strokeWidth(2)
    rect(M+M, M+M, W-(4*M), H-(4*M))
    stepX, stepY = 0, 0
    incX, incY = M, M
    for x in range(13):
        polygon(((M+M)+stepX, M+M),
                ((M+M)+stepX, H-(M+M)))
        stepX += incX
    for y in range(5):
        polygon((M+M, (M+M)+stepY),
                (W-(M+M), (M+M)+stepY))
        stepY += incY

# NEW PAGE
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)


font("../../fonts/variable_font/SofiaSansVF.ttf")
# Get axis from font
for axis, data in listFontVariations().items():
    print((axis, data))

# MAIN LOOP
a = 0
base_width = 0
for frame in range(F):     
    new_page()
    font("../../fonts/variable_font/SofiaSansVF.ttf")
    grid() # Toggle for grid view
    fill(0)
    #rect(M*2, M*5,M*5,M*1)
    t = 0
    f = 0
    base_width = sin(a)*10+10
    print("base_width = ",frame,base_width)
    for i in range(12):
        stroke(2)
        y = sin(a+t)*32
        f = y*0.01
        fill(0)
        stroke(0,0.5,1)
        strokeWidth(2)

        oval((M*2)+(i*64), (M*2.5)+(y), M, M)

        fill(1)
        stroke(None)
        tracking(None)
        fontSize((M*2.8))
        
        hello_width = base_width+80
        fontVariations(wght=900)
        fontVariations(wdth=hello_width)
        text("Hello", (M*2, M*3.45))
        
        world_width = 100-base_width
        fontVariations(wght=900)
        fontVariations(wdth=world_width) 
        text("World", ((M*6.58)+(base_width*6), M*3.45)) 
        t += 0.1
    #print(y)
    a += 0.2

saveImage("17.gif")