# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/
# 🌍 GIT URL: https://github.com/eliheuer/drawbot-sketchbok
# ✅ July 23rd

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN
W, H, M = 1000, 1000, 100

# Set variation
# fontVariations(wght=700)

# EDGE #########################################################################
def edge():
    #960, 704
    stroke(0.5)
    strokeWidth(1)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID #########################################################################
def grid():
    stroke(0.5)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = M/4, M/4
    for x in range(32):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(132):
        polygon((M, M+stpY), (W-M, M+stpY))
        stpY += incY


# BASIC_PAGE ##################################################################
def new_page():
    newPage(W, H)
    fill(0)
    rect(-2, -2, W+2, H+2)
    # LOAD BASIC FONT
    # Fonts
    # font("fonts/BlobGX.ttf")
    # Set axis from font
    for axis, data in listFontVariations().items():
        print((axis, data))
    # font("fonts/Blob-Black.ttf")  # Set the font
    # font("fonts/a.ttf")  # Set the font
    # Set variation 
    # fontVariations(wght=500)



# Page ########################################################################
new_page()

stroke(0.5)

#grid() # Toggle for grid view
#edge() # Toggle for safe area

stroke(0)
X = 5.75
B = 0
for i in range(10):
    fill(1,B,0)
    oval(M*7,M*X,M/2,M/2)
    X -= 0.25
    B += 0.1

font("../../fonts/bluu/BluuNext-Bold.otf")
fontSize(24)
fill(1)
stroke(None)
tracking(-5.0)
fontSize((M*1))
text("Dougal & Gammer",     M, (M*5))
text("Fires in the Sky",     M, (M*4.25))
fontSize(M*0.3)
tracking(-2)
text("Raver Baby",     M*7.52, (M*4.75))
fontSize(M*1)
tracking(-14.0)
#text("A",             M*4.65, (M*4))

fontSize(24)
tracking(None)
font("InputMono")
text("BABY014",             M*7.52, (M*4.5))
text("45 RPM",             M*7.52, (M*4.25))
saveImage("elih-dbsb-19-07-23.png")

