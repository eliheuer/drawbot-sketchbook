# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/
# 🌍 GIT URL: https://github.com/eliheuer/drawbot-sketchbok
# ✅ July 23rd

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN
W,H, M = 1000, 512, 100

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
image("../../images/thaw.jpg", (0, -200), alpha=1)
stroke(0.5)

#grid() # Toggle for grid view
#edge() # Toggle for safe area

font("../../fonts/bluu/BluuNext-Bold.otf")
fontSize(24)
fill(1)
stroke(None)
tracking(-2.0)
fontSize((M*0.5))
text("“Seek a furnace,",     M-18, (M*4.5))
text("but it would burn you.",     M, (M*4))
text("You only need the flame of a lamp.”",    M, (M*3.5))
text("",     M, (M*3))
text("—Rumi",     M, (M*1))


saveImage("elih-dbsb-19-07-24.png")

