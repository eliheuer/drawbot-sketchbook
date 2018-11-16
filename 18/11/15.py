# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLE
W,H,M,F = 1000,1000,20,30     # WIDTH, HEIGHT, MARGIN, FRAMES
VAR_WGHT = 100                # VARIABLE FONT WEIGHT
LINE_H = H/10                 # LINE HEIGHT
U = 32
START_POS = (U*28)+M 

# SET FONT
font("Inter-UI.var.ttf")
for axis, data in listFontVariations().items():
    print((axis, data))

# GRID DRAWING FUNCTION
def grid(inc):
    stroke(0)
    strokeWidth(2)
    stpX, stpY = 0, 0
    incX = (W-(M*2))/inc
    incY = (W-(M*2))/inc
    print("incX=", incX)
    for x in range(inc+1):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(inc+1):
        polygon((M, M+stpY), (H-M, M+stpY))
        stpY += incY

def set_box_style_a():
    fill(0.9,0.1,0)
    stroke(0.9,0.1,0)

def set_box_style_b():
    fill(1)
    stroke(0)

def draw_boxes():
    # ROW 1  (x, y, w, h)
    set_box_style_b()
    rect(M+(U*2), M+(U*18), (U*24),  (U*6) )
    #rect(M+(U*4), M+(U*18), (U*24),  (U*6) )
    for i in range(9):
        rect(M+(U*i), M+(U*i),  (U*i),  (U*i) )

# DRAW NEW PAGE
newPage(W, H)
fill(1)
rect(0, 0, W, H)
grid(30)
draw_boxes()
fill(0)

# aaaaaaaaaaaaaaaaaa
fill(0)
fontSize(240)
wght_var = 400
stroke(1)
strokeWidth(1)
for i in range(10):
    fontVariations(wght=wght_var)
    text("a", ( M+(U*2.13)+(U*(i*2.13)), (U*19)+M ))
    wght_var += 50
    print("a=", wght_var)

stroke(0)
oval(M+(U*26), M, U*4, U*4)

# Save GIF
saveImage("15.gif")
# saveImage("basic-specimen.pdf")
# saveImage("basic-specimen.png")
