# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os

# STATIC VARIABLE
W, H, M, F = 1000, 1000, 100, 100
VAR = 100
DOT =  19
AMP = 300
STP = 0
XPO = 0
YPO = 0

# SET FONT
font("Helvetica Neue")
for axis, data in listFontVariations().items():
    print((axis, data))

# GRID
def grid(INC):
    # SET STYLE
    lineCap("round")
    stroke(0.5)
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
    frameDuration(1/30)
    fill(0)
    rect(0, 0, W, H)

def draw_dot(X, Y):
    oval(int(X)+(W/2), int(Y)+(W/2), DOT, DOT)

r = 0 
for frame in range(F):
    TRI_ROT = (math.pi/3)*2
    # Draw PAGE
    new_page()
    strokeWidth(1)
    grid(9)

    # SET DOT POS
    XPO_A = (math.cos(STP) * AMP)-DOT/2
    YPO_A = (-1 * math.sin(STP) * AMP)-DOT/2

    XPO_B = (math.cos(STP+(TRI_ROT)) * AMP)-DOT/2
    YPO_B = (-1 * math.sin(STP+(TRI_ROT)) * AMP)-DOT/2

    XPO_C = (math.cos(STP-(TRI_ROT)) * AMP)-DOT/2
    YPO_C = (-1 * math.sin(STP-(TRI_ROT)) * AMP)-DOT/2

    # DRAW LINES + DOT
    for i in range(3):
        #draw_lines( (XPO) - DOT/2, (YPO) - DOT/2 )
        rotate(40, center=(W/2, H/2))
        stroke(1)
        fill(1)
        strokeWidth(4)

        polygon((int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)),
                (int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)))
        polygon((int(XPO_B+(DOT/2))+(W/2), int(YPO_B+(DOT/2))+(W/2)),
                (int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)))
        polygon((int(XPO_C+(DOT/2))+(W/2), int(YPO_C+(DOT/2))+(W/2)),
                (int(XPO_A+(DOT/2))+(W/2), int(YPO_A+(DOT/2))+(W/2)))

        draw_dot(XPO_A, YPO_A)
        draw_dot(XPO_B, YPO_B)
        draw_dot(XPO_C, YPO_C)
        STP += (0.003) * math.pi

saveImage("14.gif")
