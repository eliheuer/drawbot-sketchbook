# 📄 RENDER THIS DOCUMENT WITH DRAWBOT (Python 3): http://www.drawbot.com/
# 🌍 GIT URL: https://github.com/eliheuer/drawbot-sketchbok
# ✅ July 23rd

from drawBot import *
import math

# [W] WIDTH, [H] HEIGHT, [M] MARGIN
W,H, M = 1000, 500, 20

# Set variation
# fontVariations(wght=700)

# EDGE #########################################################################
def edge():
    #960, 704
    stroke(0.1)
    strokeWidth(1)
    fill(None)
    rect(M, M, W-(2*M), H-(2*M))

# GRID #########################################################################
def grid():
    stroke(0.1)
    strokeWidth(1)
    stpX, stpY = 0, 0
    incX, incY = M, M
    for x in range(48):
        polygon((M+stpX, M), (M+stpX, H-M))
        stpX += incX
    for y in range(32):
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
image("../../images/thaw.jpg", (0, -200), alpha=0.9)
#grid() # Toggle for grid view
#edge() # Toggle for safe area

font("../../fonts/bluu/BluuNext-Titling.ttf")
fill(1)
stroke(None)
tracking(-1.0)
fontSize((M*7))
text("Dare to be naïve.", 2.8*M, (M*10))
#rect(M,M,M*9,M*9)
#rect(15*M,15*M,M*9,M*9)

saveImage("elih-dbsb-19-07-29.png")

