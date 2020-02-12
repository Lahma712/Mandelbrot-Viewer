from PIL import Image
from PIL import ImageDraw
import getpass
host = getpass.getuser()
def mandelbrot(c,maxIt):
    z = 0
    n = 0
    while abs(z) <= 2 and n < maxIt:
        z = z * z + c
        n += 1
    return n

maxIt = int(input("Iteration depth: "))
Q = input("Colors? y/n ")
if Q == "y":
    offset = int(input("Background color (Red:0-15|Yellow:15-50|Green:50-110|Blue:110-170|Violet:170-240|Red:240-250): "))
    light = int(input("Lightness (0-255) : "))
    glow = int(input("White glow (positive integer between 0-20 f.ex): "))
else:
    Q2 = (input("Options:\n-White outlines on black background (wout) \n-Black outlines on white background (bout) \n-Black on white background (b)\n-White on black background (w)\n")).lower()
    glow = int(input("glow (positive integer between 1-10 f.ex): "))
    if glow == 0:
        glow = 1

W = int(input("Width of resolution (pixels): "))
H = int(input("Height of resolution (pixels): "))
ratio = float(H/W)
xStart = float(input("Start value for X: "))
xEnd = float(input("End value for X: "))
xDist = abs(xStart -xEnd)
yDist = xDist * ratio
yvalue = float(input("Y value (= will be the middle of the screen): "))
img = Image.new('HSV', (W, H))
draw = ImageDraw.Draw(img)

for x in range(0, W):
    for y in range(0, H):
        c = complex(xStart + abs(xDist) * (x / W), (yvalue + (yDist/2)) - yDist * (y / H))
        cIt = mandelbrot(c,maxIt)

        color = int((255 * cIt) / maxIt)
        if Q == "n":
            if Q2 == "wout":
                draw.point([x, y], (0, 0, 0 if cIt == maxIt else glow*color))
            elif Q2 == "bout":
                draw.point([x, y], (0, 0, 255 if cIt == maxIt else 255-glow*color))
            elif Q2 == "b":
                draw.point([x, y], (0, 0, 0 if cIt == maxIt else 255 - glow*color))
            elif Q2 == "w":
                draw.point([x, y], (0, 0, 255 if cIt == maxIt else glow * color))
        else:

            if color + offset > 255:
                Color = (color+offset)-255
            else:
                Color = color+offset
            saturation = 255 - glow * color
            draw.point([x, y], (Color, saturation, 0 if cIt == maxIt else light))

img.convert('RGB').save("c:\\Users\\{}\\Desktop\\image.png".format(host))
img.show()
