# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLE
W, H, M, F = 1000, 1000, 100, 100
VAR = 100
DOT =  16
AMP = 300
STP = 0
XPO = 0
YPO = 0

# SET FONT
font("Helvetica Neue")
#for axis, data in listFontVariations().items():
#    print((axis, data))

# GRID
def grid(INC):
    # SET STYLE
    lineJoin("round")
    lineCap("round")
    stroke(0.3)
    STX, STY = 0, 0
    INX, INY = (W-(M*2))/INC, (H-(M*2))/INC
    for x in range(INC+1):
        polygon((M+STX, M), (M+STX, H-M))
        STX += INX
    for y in range(INC+1):
        polygon((M, M+STY), (H-M, M+STY))
        STY += INY

# NEW PAGE
def new_page(): 
    newPage(W, H)
    frameDuration(1/24)
    fill(0)
    rect(0, 0, W, H)

def draw_dot(X, Y):
    fill(1,0,0)
    stroke(None)
    oval(int(X)+(W/2), int(Y)+(W/2), DOT, DOT)

def draw_lines(X, Y):
    fill(None)
    stroke(1,0,0)
    #line((W/2, W/2), 
    #    ( int(X) + ( W/2 + DOT/2 ), int(Y) + ( W/2 + DOT/2 )))
    #line((W/2, W/2), 
    #    ( int(X) + ( W/2 + DOT/2 ), W/2))
    #line((int(X) + (W/2+DOT/2), W/2), 
    #    (int(X) + (W/2+DOT/2), int(Y) + (W/2+DOT/2)))

    fill(1,1,0)
    oval((W/2)-DOT/2, (W/2)-DOT/2, DOT, DOT)
    oval(int(X) + (W/2), (W/2)-DOT/2, DOT, DOT)
    #oval(M*2, M*2, W/2, H/2)

r = 0 
for frame in range(F):
    # SET STYLE
    #lineJoin("round")
    #lineCap("round")
    # Draw PAGE
    new_page()
    strokeWidth(1)
    grid(20)
    # SET DOT POS
    XPO = math.cos(STP) * AMP
    YPO = -1 * math.sin(STP) * AMP
    XPO_STR = "{:.3f}".format(XPO)
    YPO_STR = "{:.3f}".format(YPO)
    print("XPO: ", XPO_STR)
    print("YPO: ", YPO_STR)
    # DRAW LINES + DOT

    for i in range(9):
        rotate(40, center=(W/2, H/2))
        draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        draw_dot(   (XPO) - DOT/2, (YPO) - DOT/2 )  

    STP += 0.02 * math.pi

saveImage("13b.gif")
