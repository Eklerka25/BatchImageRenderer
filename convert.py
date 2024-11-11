from PIL import Image
import os

ANSI_COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (255, 255, 0),
    (0, 0, 255),
    (255, 0, 255),
    (0, 255, 255),
    (192, 192, 192),
    (128, 128, 128),
    (255, 0, 0),
    (0, 255, 0),
    (255, 255, 0),
    (0, 0, 255),
    (255, 0, 255),
    (0, 255, 255),
    (255, 255, 255)
]

def fcm(rgb):
    r, g, b = rgb
    minDist = float('inf')
    clst = None
    for color in ANSI_COLORS:
        cr, cg, cb = color
        dist = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
        if dist < minDist:
            minDist = dist
            clst = color
    return clst

def toBir(imagePath, outputPath, width=340, height=115):
    image = Image.open(imagePath)
    
    image = image.resize((width, height))
    image = image.convert('RGB')

    with open(outputPath, 'w') as f:
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.getpixel((x, y))
                f.write(f"{r};{g};{b}\n")

def toBir_ansi(imagePath, outputPath, width=350, height=125):
    image = Image.open(imagePath)
    
    image = image.resize((width, height))
    image = image.convert('RGB')

    with open(outputPath, 'w') as f:
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.getpixel((x, y))
                clst = fcm((r, g, b))
                f.write(f"{clst[0]};{clst[1]};{clst[2]}\n")

inputFile = "image.png"
outputFile = "image.bir"
toBir(inputFile, outputFile)
