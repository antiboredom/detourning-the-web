from PIL import Image, ImageDraw, ImageFont
import sys

def drawtext(filename, text):
    im = Image.open(filename)
    canvas = ImageDraw.Draw(im)

    fnt = ImageFont.truetype('/Users/sam/Library/Fonts/Lato-Bold.ttf', 60)

    canvas.text((10, 10), text, font=fnt, fill=(0,0,0))

    canvas.rectangle([(100, 100), (500, 500)], fill=(255, 0, 0))

    im.save(filename+'.withtext.jpg')

drawtext(sys.argv[1], sys.argv[2])
